import paho.mqtt.client as mqtt
import json
import os
import subprocess
import time
import requests
from pathlib import Path
import threading
import atexit
import base64
import re
import platform
import sys
import importlib
from datetime import datetime

import logging
# 2. 创建主入口的 logger
logger = logging.getLogger(__name__)

try:
    from unidiff import PatchSet
    UNIDIFF_AVAILABLE = True
except ImportError:
    UNIDIFF_AVAILABLE = False
    logger.warning("警告：未安装 unidiff 库，apply_patch 命令将不可用。请运行 'pip install unidiff' 安装。")

# 加载 .env 文件中的环境变量 (如果存在)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # 如果没有安装 python-dotenv，则不加载 .env 文件
    pass


# 确保当前目录在 sys.path 中，以便导入动态模块
current_dir = Path(__file__).parent.resolve()
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

def replace_placeholder_path(input_str: str, place_holder: str, file_path: str) -> str:
    """
    将输入字符串中的 {placeHolder} 占位符按规则替换为 file_path 或 file_path/

    :param input_str:   原始字符串（可能为 None）
    :param place_holder: 占位符名称（如 "baseDir"，大小写不敏感）
    :param file_path:    替换的目标路径（如 "/workfolder"）
    :return:             替换后的字符串
    """
    if input_str is None:
        return None

    # 构造正则表达式，不区分大小写，花括号在正则中不需要转义（不是量词）
    # 注意：如果 place_holder 中包含正则元字符，会与 Java 行为一致（不转义）
    pattern = re.compile(r'\{%s\}' % place_holder, re.IGNORECASE)

    result_parts = []
    last_end = 0

    for match in pattern.finditer(input_str):
        start = match.start()
        end = match.end()

        # 添加占位符之前的普通文本
        result_parts.append(input_str[last_end:start])

        # 判断占位符后面的字符
        if end < len(input_str):
            next_char = input_str[end]
            if next_char == '/':
                # 场景1: {placeHolder}/ → 替换为 file_path/ ，同时消耗掉这个斜杠
                replacement = file_path + '/'
                last_end = end + 1   # 跳过占位符和后面的斜杠
            elif next_char != ' ':
                # 场景2: {placeHolder} 后跟非空格、非斜杠、非结束 → 替换为 file_path/ ，不消耗后面的字符
                replacement = file_path + '/'
                last_end = end        # 仅跳过占位符
            else:
                # 场景3: {placeHolder} 后跟空格 → 替换为 file_path ，不消耗空格
                replacement = file_path
                last_end = end
        else:
            # 字符串结束：{placeHolder} 在末尾 → 替换为 file_path
            replacement = file_path
            last_end = end

        result_parts.append(replacement)

    # 添加剩余未处理的文本
    result_parts.append(input_str[last_end:])
    return ''.join(result_parts)

class ToolCallHandler:
    # 常量定义
    SKILLS_WORKSPACE = "SKILLS_WORKSPACE"
    COMMAND_READ_FILE = "read_file"
    COMMAND_WRITE_FILE = "write_file"
    COMMAND_DELETE_FILE = "delete_file"
    COMMAND_EXECUTE_BASH = "execute_bash"
    COMMAND_DOWNLOAD_FILE = "download_file"
    COMMAND_UPLOAD_FILE = "upload_file"
    COMMAND_APPLY_PATCH = "apply_patch"
    COMMAND_CHAT_COMPLETION = "chat_completion"
    COMMAND_OUTPUT_STEP = "output_step"

    COMMAND_PARAM_SKILL_ID = "skill_id"
    COMMAND_PARAM_FROM_TEMPLATE = "from_template"
    COMMAND_PARAM_WORKSPACE = "workspace"
    COMMAND_PARAM_READ_FILE_FILE_PATH = "file_path"
    COMMAND_PARAM_WRITE_FILE_FILE_PATH = "file_path"
    COMMAND_PARAM_WRITE_FILE_CONTENT = "content"
    COMMAND_PARAM_WRITE_FILE_APPEND = "append"
    COMMAND_PARAM_EXECUTE_BASH_COMMAND = "command"
    COMMAND_PARAM_EXECUTE_BASH_ENV = "env"
    COMMAND_PARAM_DOWNLOAD_FILE_INDEX = "index"
    COMMAND_PARAM_DOWNLOAD_FILE_SIZE = "size"
    COMMAND_PARAM_APPLY_PATCH_NEW_FILE_PATH = "new_file_path"
    COMMAND_PARAM_APPLY_PATCH_UNIFIED_DIFF = "unified_diff"
    COMMAND_PARAM_CHAT_COMPLETION_REQUEST = "request"
    COMMAND_PARAM_CHAT_COMPLETION_AGENT_TAG = "agent_tag"
    COMMAND_PARAM_OUTPUT_STEP_CONTENT = "content"
    COMMAND_PARAM_OUTPUT_STEP_REASONING_CONTENT = "reasoning_content"
    COMMAND_PARAM_OUTPUT_STEP_SOURCE_CHANNEL = "source_channel"

    def __init__(self, skills_workspace_path=None, mqtt_url=None, skills_base_path=None):
        # 初始化时先不解析URL，等待start_listening中读取环境变量后统一处理
        # 使用传入参数（通常为None）或环境变量将在start_listening中处理
        self.skills_workspace_path = Path(skills_workspace_path).resolve() if skills_workspace_path else None
        self.skills_base_path = Path(skills_base_path).resolve() if skills_base_path else None
        self.mqtt_url = mqtt_url
        self.mqtt_host = None
        self.mqtt_port = None
        self.mqtt_path = None

        # 初始化MQTT客户端
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, transport="websockets")
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        self.client.on_socket_open = self._on_socket_open
        self.client.on_socket_close = self._on_socket_close
        self.client.reconnect_delay_set(min_delay=1, max_delay=60)

        # 新增：注册信息存储
        self.registration_data = None
        self.aifactory_url = None
        self.aifactory_token = None

        # 添加标志位跟踪连接状态
        self.is_connected = False
        self.should_stop = False
        self.is_reinitializing = False
        self.heartbeat_timer = None # 心跳定时器
        self.bot_plugins = []

        self.atexit_register = False
        self.load_bot_plugins = False

    def _on_connect(self, client, userdata, flags, reason_code, properties):
        """MQTT连接回调"""
        if reason_code == 0:
            logger.info(f"已连接到MQTT WebSocket服务器 {self.mqtt_host}:{self.mqtt_port}{self.mqtt_path}")
            # 使用注册获取的 listen_topic 进行订阅
            if self.registration_data and 'listen_topic' in self.registration_data:
                topic = self.registration_data['listen_topic']
                client.subscribe(topic)
                logger.info(f"已订阅动态主题: {topic}")
                self.is_connected = True
            else:
                logger.error("错误：未获取到注册信息，无法订阅主题")
                self.is_connected = False
        else:
            logger.error(f"连接失败，返回码: {reason_code}")
            self.is_connected = False

    def _on_disconnect(self, client, userdata, flags, reason_code, properties):
        """MQTT断开连接回调"""
        logger.warning(f"与MQTT服务器断开连接，原因码: {reason_code}")
        self.is_connected = False

        # 如果不是主动停止，则尝试重连
        if not self.should_stop:
            logger.info("尝试重新连接...")
            # 重连是自动的，因为设置了reconnect_delay_set

    def _on_socket_open(self, client, userdata, sock):
        """Socket打开回调"""
        logger.info("WebSocket连接已打开")

    def _on_socket_close(self, client, userdata, sock):
        """Socket关闭回调"""
        logger.warning("WebSocket连接已关闭")
        self.is_connected = False

    def _try_send_active(self):
        """异步发送激活信号（不阻塞调用线程）"""
        def send_active_task():
            if self.should_stop:
                return

            url = f"{self.aifactory_url}/{self.aifactory_token}/active"
            current_skills = self._load_skills_manifest()

            if not self.registration_data:
                return

            active_payload = dict(self.registration_data)
            active_payload['skills'] = current_skills

            try:
                requests.post(url, json=active_payload, timeout=10)
            except Exception as e:
                logger.error(f"发送激活信号时发生错误: {e}")

        # 启动守护线程，主线程退出时自动结束
        threading.Thread(target=send_active_task, daemon=True).start()

    def _start_heartbeat(self):
        """启动心跳机制（每60秒发送一次激活信号）"""
        self.should_stop = False
        def send_active():
            if self.should_stop:
                return

            _next_heartbeat = False
            try:
                url = f"{self.aifactory_url}/{self.aifactory_token}/active"

                 # 获取当前最新的技能清单
                current_skills = self._load_skills_manifest()

                # 构建激活数据：保留原有注册信息，添加 skills 字段
                if self.registration_data:
                    active_payload = dict(self.registration_data)
                    active_payload['skills'] = current_skills
                else:
                    # 理论上注册成功后才启动心跳，此处防御
                    logger.info("触发重新初始化流程...")
                    self.reinitialize() # 调用重新初始化
                    return # 结束当前心跳，避免继续启动定时器

                response = requests.post(url, json=active_payload, timeout=10)

                # --- 核心修改点：处理纯文本响应 ---
                # 假设服务器直接返回 "true" 或 "false" 字符串
                response_text = response.text.strip().lower()

                if response.status_code == 200:
                    if response_text == "true":
                        logger.info("成功发送激活信号 (Heartbeat)")
                        _next_heartbeat = True
                    else:
                        # 返回不是 "true" (即 "false" 或其他)
                        logger.error(f"激活信号校验失败，服务器返回: '{response_text}' (非 true)")
                        logger.info("触发重新初始化流程...")
                        self.reinitialize() # 调用重新初始化
                        return # 结束当前心跳，避免继续启动定时器
                else:
                    logger.error(f"激活信号发送失败，HTTP状态码: {response.status_code}")
                    # 这里不直接 reinitialize，让 MQTT 的断连重连机制处理，或者根据需要开启
                    # 如果希望 HTTP 失败也强制重置，可以取消下面的注释
                    self.reinitialize()
                    return

            except Exception as e:
                logger.error(f"发送激活信号时发生错误: {e}")
                # 网络异常通常由 MQTT on_disconnect 处理，这里也可以选择重置
                self.reinitialize()
                return
            finally:
                # 只有在没有触发重新初始化且未停止的情况下，才启动下一次心跳
                if _next_heartbeat:
                    if self.heartbeat_timer:
                        self.heartbeat_timer.cancel()
                        self.heartbeat_timer = None
                    self.heartbeat_timer = threading.Timer(60.0, send_active)
                    self.heartbeat_timer.start()
                else:
                    print("已停止心跳，跳过本次心跳")

        # 启动第一次心跳
        send_active()
    # --- 新增：重新初始化方法 ---
    def reinitialize(self):
        """
        执行完整的重新初始化流程。
        这是一个高风险操作，需要防止递归爆炸。
        """
        # 防止多次并发触发
        if self.is_reinitializing:
            logger.warning("重入保护：当前正在进行重新初始化，忽略新的触发请求。")
            return
        self.is_reinitializing = True

        logger.info("【重新初始化】流程启动...")

        # 1. 标记停止，防止旧线程干扰
        self.should_stop = True

        # 2. 清理资源
        # 取消当前的心跳定时器
        if self.heartbeat_timer:
            self.heartbeat_timer.cancel()
            self.heartbeat_timer = None

        # 断开 MQTT 连接
        try:
            self.client.disconnect()
            # 立即停止 loop，不等待后台线程
            self.client.loop_stop(force=True)
        except:
            pass

        # 尝试注销 (尽力而为)
        self._unregister_skill_runner()

        logger.info("【重新初始化】清理完成，准备重启...")

         # 新增：注册信息存储
        self.registration_data = None
        self.aifactory_url = None
        self.aifactory_token = None

        # 添加标志位跟踪连接状态
        self.is_connected = False
        self.should_stop = False
        self.is_reinitializing = False
        self.heartbeat_timer = None # 心跳定时器

        # 4. 重新执行核心逻辑
        self.start_listening()

    def _load_skills_manifest(self):
        """
        扫描 skills_base_path 下的每个子目录，读取 SKILL.md 文件，
        提取开头的 --- ... --- 块中的 YAML 元数据。
        返回格式: { skill_id: metadata_dict }
        """
        if not self.skills_base_path:
            logger.warning("警告：skills_base_path 未设置，无法加载技能清单")
            return {}

        manifest = {}
        skills_root = Path(self.skills_base_path)
        if not skills_root.exists() or not skills_root.is_dir():
            logger.warning(f"技能根目录不存在或不是目录: {skills_root}")
            return {}

        # 遍历一级子目录（每个技能一个文件夹）
        for skill_dir in skills_root.iterdir():
            if not skill_dir.is_dir():
                continue

            # 忽略隐藏目录及点号开头的文件夹
            if skill_dir.name.startswith('.') or skill_dir.name.startswith('_'):
                logger.warning(f"忽略目录 {skill_dir.name}")
                continue
            skill_id = skill_dir.name
            skill_md_path = skill_dir / "SKILL.md"
            if not skill_md_path.exists():
                logger.warning(f"技能目录 {skill_id} 中未找到 SKILL.md，跳过")
                continue

            try:
                content = skill_md_path.read_text(encoding='utf-8')
                metadata = self._extract_yaml_from_skill_md(content)
                if metadata:
                    # 附加当前文件的最后修改时间（yyyy-mm-dd HH:mm:ss）至最后
                    metadata += "\nlast_modified: {}".format(datetime.fromtimestamp(skill_md_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S"))
                    manifest[skill_id] = metadata
                else:
                    logger.warning(f"技能 {skill_id} 的 SKILL.md 中未找到有效的 YAML 元数据块")
            except Exception as e:
                logger.error(f"读取技能 {skill_id} 的 SKILL.md 时出错: {e}")
                continue

        logger.info(f"已加载技能清单，共 {len(manifest)} 个技能")
        return manifest

    def _extract_yaml_from_skill_md(self, content):
        """
        从 SKILL.md 内容中提取开头的 YAML front matter 块：
        ---
        key: value
        ---
        返回解析后的字典，若未找到或解析失败则返回 None。
        """
        # 匹配文件开头的 --- ... --- 块
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
        if not match:
            return None
        yaml_block = match.group(1).strip()
        if not yaml_block:
            return None

        return yaml_block


    def _register_skill_runner(self):
        """向服务器注册SkillRunner"""
        try:
            url = f"{self.aifactory_url}/{self.aifactory_token}/register"

            # 加载本地技能清单
            skills_manifest = self._load_skills_manifest()

            registration_data = {
                "workspace": str(self.skills_workspace_path),
                "skills_path":  str(self.skills_base_path) if self.skills_base_path else "",
                "os_type": platform.system(),
                "skills": skills_manifest
            }
            response = requests.post(url, json=registration_data, timeout=10)
            if response.status_code == 200:
                self.registration_data = response.json()
                logger.info(f"注册成功！获取监听主题: {self.registration_data.get('listen_topic')}")
                return True
            else:
                logger.error(f"注册失败，HTTP状态码: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"注册过程中发生错误: {e}")
            return False

    def _unregister_skill_runner(self):
        """向服务器注销SkillRunner"""
        if self.registration_data and self.aifactory_url and self.aifactory_token:
            try:
                url = f"{self.aifactory_url}/{self.aifactory_token}/unregister"
                response = requests.post(url, json=self.registration_data, timeout=10)
                if response.status_code == 200:
                    logger.info("成功发送注销信号")
                else:
                    logger.error(f"注销失败，状态码: {response.status_code}")
            except Exception as e:
                logger.error(f"注销过程中发生错误: {e}")

    def start_listening(self):
        """开始监听MQTT消息（包含注册和心跳逻辑）"""
        # 1. 读取环境变量
        self.aifactory_url = os.getenv('AIFACTORY_URL')
        self.aifactory_token = os.getenv('AIFACTORY_TOKEN')

        # 读取配置，不再提供默认值，强制要求环境变量设置
        env_mqtt_url = os.getenv('AIFACTORY_MQTT')
        env_skills_base_path = os.getenv('AIFACTORY_SKILLS')
        env_skills_workspace_path = os.getenv('AIFACTORY_SKILL_WORKSPACE')

        if not self.aifactory_url or not self.aifactory_token:
            logger.error("错误：请设置环境变量 AIFACTORY_URL 和 AIFACTORY_TOKEN")
            return
        if not env_mqtt_url or not env_skills_base_path or not env_skills_workspace_path:
            logger.error("错误：请设置环境变量 AIFACTORY_MQTT, AIFACTORY_SKILLS, AIFACTORY_SKILL_WORKSPACE")
            return

        # 重新初始化实例变量，使用环境变量
        self.skills_workspace_path = Path(env_skills_workspace_path).resolve()
        self.skills_base_path = Path(env_skills_base_path).resolve()

        # 确保工作目录存在
        self.skills_workspace_path.mkdir(parents=True, exist_ok=True)

        # 解析MQTT URL (使用环境变量)
        from urllib.parse import urlparse
        parsed_url = urlparse(env_mqtt_url)
        self.mqtt_host = parsed_url.hostname
        self.mqtt_port = parsed_url.port
        self.mqtt_path = parsed_url.path or "/mqtt"

        logger.info(f"使用MQTT URL: {env_mqtt_url}")
        logger.info(f"使用Skills根目录: {self.skills_base_path}")
        logger.info(f"使用Skills工作空间: {self.skills_workspace_path}")

        # 2. 注册 SkillRunner，如果失败则Sleep 5秒后重试
        while True:
            if self._register_skill_runner():
                break
            logger.error("注册失败，正在重试...")
            time.sleep(5)
        # if not self._register_skill_runner():
        #    print("无法注册SkillRunner，程序退出")
        #    return

        # 3. 注册退出回调（确保程序正常结束或Ctrl+C时注销）
        if self.atexit_register is False:
            atexit.register(self._unregister_skill_runner)
            self.atexit_register = True

        # 4. 启动心跳线程
        self._start_heartbeat()

        # 启动机器人插件
        if self.load_bot_plugins is False:
            self._load_bot_plugins()
            self.load_bot_plugins = True

        # 5. 开始MQTT循环
        try:
            self.client.ws_set_options(path=self.mqtt_path)
            self.client.connect(self.mqtt_host, self.mqtt_port, 60)
            logger.info("开始监听MQTT消息...")
            self.client.loop_forever()
            logger.info("MQTT循环已结束")
        except KeyboardInterrupt:
            logger.warning("\n收到中断信号，正在退出...")
        finally:
            try:
                self.should_stop = True
                # 取消心跳定时器
                if self.heartbeat_timer:
                    self.heartbeat_timer.cancel()
                    self.heartbeat_timer = None
                # 手动调用注销（atexit会自动触发，但显式调用更保险）
                self._unregister_skill_runner()
                self.client.disconnect()
                logger.warning("已断开连接")
            except :
                pass


    def _on_message(self, client, userdata, msg):
        """MQTT消息接收回调"""
        try:
            payload_str = msg.payload.decode('utf-8')
            logger.info(f"收到消息 - 主题: {msg.topic}, 载荷: {payload_str}")

            # 解析消息为JSON
            message_data = json.loads(payload_str)

            # 提取command和args
            command = message_data.get('command')
            tool_call_id = message_data.get('tool_call_id')
            result_topic = message_data.get('result_topic')
            args = message_data.get('args', {})
            scope = message_data.get('scope')
            if scope:
                args["_scope"] = scope
            # 获取扩展内容，extended 对象存储了相对于技能的文件路径及内容
            extended = message_data.get('extended')

            if not command:
                logger.warning("消息中缺少command字段")
                return

            skill_id = args.get(self.COMMAND_PARAM_SKILL_ID)
            if not skill_id:
                raise Exception("未传入技能标识")

            # 写入扩展文件至技能目录
            if extended is not None and not self.SKILLS_WORKSPACE == skill_id:
                # 写入扩展文件
                skill_folder = self.skills_base_path / skill_id
                # extended 是一个字典，键是相对于技能目录的文件路径，值是文件内容
                for relative_path, content in extended.items():
                    # 解析实际路径
                    real_path = skill_folder / relative_path
                    # 确保父目录存在
                    real_path.parent.mkdir(parents=True, exist_ok=True)
                    # 写入文件
                    real_path.write_text(content, encoding='utf-8')
                    logger.info(f"已写入扩展文件: {real_path.resolve()}")


            # 如果有result_topic，则记录日志
            if result_topic:
                logger.info(f"工具调用ID: {tool_call_id}, 结果将发送至: {result_topic}")

            # 调用工具处理函数
            try:
                # 判断是否为上传文件
                if command == self.COMMAND_UPLOAD_FILE:
                    result = self._upload_file(args, tool_call_id, result_topic)
                else:
                    result = self.on_tool_call(command, args)
                logger.info(f"工具调用结果: {result}")

                # 如果指定了结果主题，则发送结果
                if result_topic and tool_call_id:
                    response_data = {
                        "tool_call_id": tool_call_id,
                        "result": result,
                        "error": False  # 成功执行
                    }
                    self._send_result(result_topic, response_data)

            except Exception as e:
                error_result = f"工具调用失败: {str(e)}"
                logger.error(error_result)

                # 如果指定了结果主题，则发送错误结果
                if result_topic and tool_call_id:
                    error_response = {
                        "tool_call_id": tool_call_id,
                        "result": error_result,
                        "error": True  # 标记为错误
                    }
                    self._send_result(result_topic, error_response)

        except json.JSONDecodeError:
            logger.error("消息不是有效的JSON格式")
        except Exception as e:
            logger.error(f"处理消息时发生错误: {str(e)}")

    def _send_result(self, result_topic, response_data):
        """发送结果到指定主题"""
        try:
            result_payload = json.dumps(response_data, ensure_ascii=False)
            self.client.publish(result_topic, result_payload)
            logger.info(f"已发送结果到主题 '{result_topic}': {result_payload}")
        except Exception as e:
            logger.error(f"发送结果失败: {str(e)}")

    def on_tool_call(self, command, args):
        """处理工具调用"""
        skill_id = args.get(self.COMMAND_PARAM_SKILL_ID)
        if not skill_id:
            raise Exception("未传入技能标识")

        from_template = args.get(self.COMMAND_PARAM_FROM_TEMPLATE)
        if from_template:
            from_template = from_template.lower() == "true" # 转换为布尔值
        else:
            from_template = False

        current_workspace_path = args.get(self.COMMAND_PARAM_WORKSPACE)
        current_workspace_dir = Path(self.skills_workspace_path).resolve()
        if current_workspace_path and len(current_workspace_path) > 0:
            # 判断目录是否存在，没有则新建
            current_workspace_dir = Path(current_workspace_path).resolve()
            current_workspace_dir.mkdir(parents=True, exist_ok=True)
        else:
            current_workspace_path = str(self.skills_workspace_path.resolve())

        scope_str = args.get("_scope")

        if scope_str:
            items = [item.strip() for item in re.split(r'[;, ]+', scope_str) if item.strip()]
            for item in items:
                if "=" in item:
                    key, val = item.split("=", 1)
                    key, val = key.strip(), val.strip()

                    if key and val:
                        target_dir = os.path.join(str(current_workspace_dir.resolve()), key.lower(), val)
                        if not os.path.exists(target_dir):
                            os.makedirs(target_dir, exist_ok=True)
                            logger.info(f"📁 已创建平行 scope 目录: {target_dir}")

        # 如果是工作区相关操作
        if self.SKILLS_WORKSPACE == skill_id:

            if self.COMMAND_EXECUTE_BASH == command:
                cmd = args.get(self.COMMAND_PARAM_EXECUTE_BASH_COMMAND)
                if not cmd:
                    raise Exception("未传入执行命令")

                file_path = args.get(self.COMMAND_PARAM_WRITE_FILE_FILE_PATH)
                file_obj = None
                if file_path and len(file_path) > 0:
                    # file_path = file_path.replace("{SKILLS_WORKSPACE}", current_workspace_path)
                    file_path = replace_placeholder_path(file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                    content = args.get(self.COMMAND_PARAM_WRITE_FILE_CONTENT, "")
                    # 解析实际路径
                    real_path = self._is_absolute_path(file_path) and file_path or \
                        str(self._resolve_to_absolute(current_workspace_dir, file_path))
                    # 验证路径是否在工作区内
                    if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                        return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                    file_obj = Path(real_path)
                    # 确保父目录存在
                    file_obj.parent.mkdir(parents=True, exist_ok=True)
                    # 写入文件
                    file_obj.write_text(content, encoding='utf-8')

                # cmd = cmd.replace("{SKILLS_WORKSPACE}", str(self.skills_workspace_path.resolve()))
                cmd = replace_placeholder_path(cmd, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))

                # 判断当前是否windows环境，如果是则替换python3为python
                if os.name == 'nt':
                    cmd = cmd.replace("python3", "python")
                try:
                    # 使用subprocess安全执行命令
                    result = subprocess.run(
                        cmd,
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=50, # 30秒超时
                    )
                    if result.returncode == 0:
                        if from_template:
                            return f"{result.stdout}"
                        if file_obj:
                            return f"写入文件[{file_obj.resolve()}]成功\n执行命令成功，返回以下内容：\n{result.stdout}"
                        return f"执行命令成功，返回以下内容：\n{result.stdout}"
                    else:
                        return f"执行命令发生错误，返回以下信息：\n{result.stderr}"
                except subprocess.TimeoutExpired:
                    return "执行命令发生错误，返回以下信息：\n命令执行超时"
                except Exception as ex:
                    return f"执行命令发生错误，返回以下信息：\n{str(ex)}"

            if self.COMMAND_READ_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                if not file_path:
                    return "读取文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                # 解析实际路径
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                # 验证路径是否在工作区内
                if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                    return f"读取文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                file_obj = Path(real_path)
                if file_obj.exists():
                    content = file_obj.read_text(encoding='utf-8')
                    if from_template:
                        return content
                    return f"读取文件成功，内容如下：\n{content}"
                else:
                    return f"读取文件发生异常，返回以下信息：\n指定文件[{file_obj.resolve()}]不存在"

            if self.COMMAND_DELETE_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                if not file_path:
                    return "删除文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                # 解析实际路径
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                # 验证路径是否在工作区内
                if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                    return f"删除文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                file_obj = Path(real_path)
                if file_obj.exists():
                    file_obj.unlink()
                    if from_template:
                        return ""
                    return f"删除文件[{file_obj.resolve()}]成功"
                else:
                    return f"删除文件发生异常，返回以下信息：\n指定文件[{file_obj.resolve()}]不存在"

            elif self.COMMAND_WRITE_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_WRITE_FILE_FILE_PATH)
                if not file_path:
                    return "写入文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                content = args.get(self.COMMAND_PARAM_WRITE_FILE_CONTENT, "")
                # 解析实际路径
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                # 验证路径是否在工作区内
                if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                    return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                file_obj = Path(real_path)
                # 确保父目录存在
                file_obj.parent.mkdir(parents=True, exist_ok=True)
                # 获取附加标志
                append = args.get(self.COMMAND_PARAM_WRITE_FILE_APPEND, False)
                # 写入文件
                if append:
                    file_obj.open('a', encoding='utf-8').write(content)
                else:
                    file_obj.write_text(content, encoding='utf-8')
                if from_template:
                    return ""
                if append:
                    return f"写入文件[{file_obj.resolve()}]成功，写入长度：{len(content)}，总长度：{file_obj.stat().st_size}"
                else:
                    return f"写入文件[{file_obj.resolve()}]成功，写入长度：{len(content)}"

            elif self.COMMAND_DOWNLOAD_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_WRITE_FILE_FILE_PATH)
                if not file_path:
                    return "写入文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                content = args.get(self.COMMAND_PARAM_WRITE_FILE_CONTENT, "")
                index = args.get(self.COMMAND_PARAM_DOWNLOAD_FILE_INDEX, -1)
                # 解析实际路径
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                # 验证路径是否在工作区内
                if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                    return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"

                file_obj = Path(real_path)
                # 确保父目录存在
                file_obj.parent.mkdir(parents=True, exist_ok=True)

                if(index >=0):
                    # 如果是下载文件的第一块，先清空文件内容
                    if file_obj.exists() and index == 0:
                        file_obj.write_bytes(b'')# 清空文件内容

                    decoded_content = base64.b64decode(content)
                    with open(real_path, 'ab') as f:
                        f.write(decoded_content)

                    return f"OK[{index}]"

                if file_obj.exists():
                    size = args.get(self.COMMAND_PARAM_DOWNLOAD_FILE_SIZE, -1)
                    # 如果传入了文件大小参数，则验证文件大小是否匹配
                    if size >= 0 and file_obj.stat().st_size != size:
                        return f"写入文件[{file_obj.resolve()}]失败，文件大小不匹配，期望: {size} bytes, 实际: {file_obj.stat().st_size} bytes"
                    return f"保存下载文件[{file_obj.resolve()}]成功"
                else:
                    return f"保存下载文件[{file_obj.resolve()}]失败"

            elif self.COMMAND_APPLY_PATCH == command:
                # 获取参数（支持占位符替换）
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                new_file_path = args.get(self.COMMAND_PARAM_APPLY_PATCH_NEW_FILE_PATH)
                unified_diff = args.get(self.COMMAND_PARAM_APPLY_PATCH_UNIFIED_DIFF)

                # 参数校验
                if not file_path:
                    return "应用补丁发生异常，返回以下信息：\n未传入应用文件路径 `file_path`"
                if not new_file_path:
                    return "应用补丁发生异常，返回以下信息：\n未传入写入文件路径 `new_file_path`"
                if not unified_diff:
                    return "应用补丁发生异常，返回以下信息：\n未传入补丁内容 `unified_diff`"

                # 替换工作区占位符
                file_path = replace_placeholder_path(file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                new_file_path = replace_placeholder_path(new_file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))

                # 解析原文件绝对路径并验证是否在工作区内
                real_file_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                if not self._validate_path_in_workspace(real_file_path, current_workspace_dir):
                    return f"应用补丁发生异常，返回以下信息：\n应用文件实际路径 [{real_file_path}] 不在工作区中，禁止访问！"

                file_obj = Path(real_file_path)
                if not file_obj.exists():
                    return f"应用补丁发生异常，返回以下信息：\n应用文件 [{file_obj.resolve()}] 不存在！"

                # 解析新文件绝对路径并验证是否在工作区内
                real_new_path = self._is_absolute_path(new_file_path) and new_file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, new_file_path))
                if not self._validate_path_in_workspace(real_new_path, current_workspace_dir):
                    return f"应用补丁发生异常，返回以下信息：\n写入文件实际路径 [{real_new_path}] 不在工作区中，禁止访问！"

                new_file_obj = Path(real_new_path)
                # 确保新文件的父目录存在
                new_file_obj.parent.mkdir(parents=True, exist_ok=True)

                # 检查 unidiff 库是否可用
                if not UNIDIFF_AVAILABLE:
                    return "应用补丁失败：未安装 unidiff 库，请执行 'pip install unidiff' 后重试。"

                try:
                    # 读取原文件所有行
                    with open(file_obj, 'r', encoding='utf-8') as f:
                        original_lines = f.readlines()

                    # 应用补丁
                    patched_lines = self._apply_patch_to_lines(original_lines, unified_diff)

                    # 写入新文件
                    with open(new_file_obj, 'w', encoding='utf-8') as f:
                        f.writelines(patched_lines)

                    if from_template:
                        return ""
                    return f"应用补丁写入文件 [{new_file_obj.resolve()}] 成功"

                except Exception as e:
                    return f"应用补丁发生异常：{str(e)}"
            elif self.COMMAND_OUTPUT_STEP == command:
                # 循环调用插件的output_step
                for plugin in self.bot_plugins:
                    try:
                        plugin.output_step(args)
                    except Exception as e:
                        logger.error(f"插件 {plugin.__class__.__name__} 在 output_step 中发生异常: {e}")

                if from_template:
                      return ""
                return f"成功"


        else:
            # 其他技能处理
            skill_folder = self.skills_base_path / skill_id

            if self.COMMAND_EXECUTE_BASH == command:
                cmd = args.get(self.COMMAND_PARAM_EXECUTE_BASH_COMMAND)
                if not cmd:
                    raise Exception("未传入执行命令")

                env = args.get(self.COMMAND_PARAM_EXECUTE_BASH_ENV)
                if not env:
                    env = {}

                env={**os.environ, **env} # 合并环境变量，优先使用传入的env
                env["SKILLS_WORKSPACE"] = str(current_workspace_dir.resolve())
                env["SKILL_BASEDIR"] = str(skill_folder.resolve())

                file_obj = None
                file_path = args.get(self.COMMAND_PARAM_WRITE_FILE_FILE_PATH)
                if file_path and len(file_path) > 0:
                    # file_path = file_path.replace("{SKILLS_WORKSPACE}", str(self.skills_workspace_path.resolve()))
                    file_path = replace_placeholder_path(file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                    content = args.get(self.COMMAND_PARAM_WRITE_FILE_CONTENT, "")
                    # 解析实际路径
                    real_path = self._is_absolute_path(file_path) and file_path or \
                        str(self._resolve_to_absolute(current_workspace_dir, file_path))
                    # 验证路径是否在工作区内
                    if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                        return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                    file_obj = Path(real_path)
                    # 确保父目录存在
                    file_obj.parent.mkdir(parents=True, exist_ok=True)
                    # 写入文件
                    file_obj.write_text(content, encoding='utf-8')

                # 替换占位符
                # cmd = cmd.replace("{baseDir}", str(skill_folder.resolve()))
                cmd = replace_placeholder_path(cmd, "baseDir", str(skill_folder.resolve()))
                cmd = replace_placeholder_path(cmd, "SKILL_BASEDIR", str(skill_folder.resolve()))
                # cmd = cmd.replace("{SKILLS_WORKSPACE}", str(self.skills_workspace_path.resolve()))
                cmd = replace_placeholder_path(cmd, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                # 判断当前是否windows环境，如果是则替换python3为python
                if os.name == 'nt':
                    cmd = cmd.replace("python3", "python")
                try:
                    # 使用subprocess安全执行命令
                    result = subprocess.run(
                        cmd,
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=50, # 30秒超时
                        # 工作目录可以设置为技能目录，避免执行环境问题
                        cwd=str(skill_folder.resolve()),
                        env=env
                    )
                    if result.returncode == 0:
                        if from_template:
                            return f"{result.stdout}"
                        if file_obj:
                            return f"写入文件[{file_obj.resolve()}]成功\n执行命令成功，返回以下内容：\n{result.stdout}"
                        return f"执行命令成功，返回以下内容：\n{result.stdout}"
                    else:
                        return f"执行命令发生错误，返回以下信息：\n{result.stderr}"
                except subprocess.TimeoutExpired:
                    return "执行命令发生错误，返回以下信息：\n命令执行超时"
                except Exception as ex:
                    return f"执行命令发生错误，返回以下信息：\n{str(ex)}"

            elif self.COMMAND_READ_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                if not file_path:
                    return "读取文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                # 解析实际路径（针对特定技能）
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(skill_folder, file_path))
                if not self._validate_path_in_workspace(real_path, skill_folder):
                    return f"读取文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在技能目录中，禁止访问！"
                file_obj = Path(real_path)
                if file_obj.exists():
                    content = file_obj.read_text(encoding='utf-8')
                    if from_template:
                        return content
                    return f"读取文件成功，内容如下：\n{content}"
                else:
                    return f"读取文件发生异常，返回以下信息：\n指定文件[{file_obj.resolve()}]不存在"

            elif self.COMMAND_DELETE_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                if not file_path:
                    return "删除文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                # 解析实际路径
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(skill_folder, file_path))
                # 验证路径是否在工作区内
                if not self._validate_path_in_workspace(real_path, skill_folder):
                    return f"删除文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在技能目录中，禁止访问！"
                file_obj = Path(real_path)
                if file_obj.exists():
                    file_obj.unlink()
                    if from_template:
                        return ""
                    return f"删除文件[{file_obj.resolve()}]成功"
                else:
                    return f"删除文件发生异常，返回以下信息：\n指定文件[{file_obj.resolve()}]不存在"

            elif self.COMMAND_WRITE_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_WRITE_FILE_FILE_PATH)
                if not file_path:
                    return "写入文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                content = args.get(self.COMMAND_PARAM_WRITE_FILE_CONTENT, "")
                # 解析实际路径（针对特定技能）
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(skill_folder, file_path))
                if not self._validate_path_in_workspace(real_path, skill_folder):
                    return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在技能目录中，禁止访问！"
                file_obj = Path(real_path)
                # 确保父目录存在
                file_obj.parent.mkdir(parents=True, exist_ok=True)
                # 获取附加标志
                append = args.get(self.COMMAND_PARAM_WRITE_FILE_APPEND, False)
                # 写入文件
                if append:
                    file_obj.open('a', encoding='utf-8').write(content)
                else:
                    file_obj.write_text(content, encoding='utf-8')
                # 判断文件名是否为SKILL.md
                if file_path == "SKILL.md":
                    # 技能已经变化，异步触发激活操作，向远程更新技能
                    self._try_send_active()

                if from_template:
                    return ""

                if append:
                    return f"写入文件[{file_obj.resolve()}]成功，写入长度：{len(content)}，总长度：{file_obj.stat().st_size}"
                else:
                    return f"写入文件[{file_obj.resolve()}]成功，写入长度：{len(content)}"
            elif self.COMMAND_APPLY_PATCH == command:
                # 获取参数（支持占位符替换）
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                new_file_path = args.get(self.COMMAND_PARAM_APPLY_PATCH_NEW_FILE_PATH)
                unified_diff = args.get(self.COMMAND_PARAM_APPLY_PATCH_UNIFIED_DIFF)

                # 参数校验
                if not file_path:
                    return "应用补丁发生异常，返回以下信息：\n未传入应用文件路径 `file_path`"
                if not new_file_path:
                    return "应用补丁发生异常，返回以下信息：\n未传入写入文件路径 `new_file_path`"
                if not unified_diff:
                    return "应用补丁发生异常，返回以下信息：\n未传入补丁内容 `unified_diff`"

                # 替换工作区占位符
                file_path = replace_placeholder_path(file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                new_file_path = replace_placeholder_path(new_file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))

                # 解析原文件绝对路径并验证是否在工作区内
                real_file_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(skill_folder, file_path))
                if not self._validate_path_in_workspace(real_file_path, skill_folder):
                    return f"应用补丁发生异常，返回以下信息：\n应用文件实际路径 [{real_file_path}] 不在技能目录中，禁止访问！"

                file_obj = Path(real_file_path)
                if not file_obj.exists():
                    return f"应用补丁发生异常，返回以下信息：\n应用文件 [{file_obj.resolve()}] 不存在！"

                # 解析新文件绝对路径并验证是否在工作区内
                real_new_path = self._is_absolute_path(new_file_path) and new_file_path or \
                    str(self._resolve_to_absolute(skill_folder, new_file_path))
                if not self._validate_path_in_workspace(real_new_path, skill_folder):
                    return f"应用补丁发生异常，返回以下信息：\n写入文件实际路径 [{real_new_path}] 不在技能目录中，禁止访问！"

                new_file_obj = Path(real_new_path)
                # 确保新文件的父目录存在
                new_file_obj.parent.mkdir(parents=True, exist_ok=True)

                # 检查 unidiff 库是否可用
                if not UNIDIFF_AVAILABLE:
                    return "应用补丁失败：未安装 unidiff 库，请执行 'pip install unidiff' 后重试。"

                try:
                    # 读取原文件所有行
                    with open(file_obj, 'r', encoding='utf-8') as f:
                        original_lines = f.readlines()

                    # 应用补丁
                    patched_lines = self._apply_patch_to_lines(original_lines, unified_diff)

                    # 写入新文件
                    with open(new_file_obj, 'w', encoding='utf-8') as f:
                        f.writelines(patched_lines)

                    if from_template:
                        return ""
                    return f"应用补丁写入文件 [{new_file_obj.resolve()}] 成功"

                except Exception as e:
                    return f"应用补丁发生异常：{str(e)}"

        raise Exception(f"未支持的指令[{command}]")

    def _upload_file(self, args, tool_call_id, result_topic):
        """处理工具调用"""
        skill_id = args.get(self.COMMAND_PARAM_SKILL_ID)
        if not skill_id:
            raise Exception("未传入技能标识")

        file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
        if not file_path:
             raise Exception("读取文件发生异常，返回以下信息：\n未传入文件路径`file_path`")

        current_workspace_path = args.get(self.COMMAND_PARAM_WORKSPACE)
        current_workspace_dir = Path(self.skills_workspace_path).resolve()
        if current_workspace_path and len(current_workspace_path) > 0:
            # 判断目录是否存在，没有则新建
            current_workspace_dir = Path(current_workspace_path).resolve()
            current_workspace_dir.mkdir(parents=True, exist_ok=True)
        else:
            current_workspace_path = str(self.skills_workspace_path.resolve())

        # 如果是工作区相关操作
        if self.SKILLS_WORKSPACE == skill_id:
            real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
            # 验证路径是否在工作区内
            if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                raise Exception(f"读取文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！")
        else:
            # 其他技能处理
            skill_folder = self.skills_base_path / skill_id
            # 解析实际路径（针对特定技能）
            real_path = self._is_absolute_path(file_path) and file_path or \
                str(self._resolve_to_absolute(skill_folder, file_path))
             # 验证路径是否在工作区内
            if not self._validate_path_in_workspace(real_path, skill_folder):
                raise Exception(f"读取文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在[{skill_id}]工作区中，禁止访问！")

        # 读取文件，按64K进行分块发送
        file_obj = Path(real_path)
        if not file_obj.exists():
            raise Exception(f"文件不存在: {real_path}")

        data = file_obj.read_bytes()
        chunk_size = 64 * 1024
        index = 0
        # 步长设为 chunk_size
        for i in range(0, len(data), chunk_size):
            chunk = data[i : i + chunk_size] # 切片操作
            response_data = {
                        "tool_call_id": tool_call_id,
                        "result": base64.b64encode(chunk).decode('utf-8'), # 将二进制数据编码为base64字符串
                        "error": False,  # 成功执行,
                        "index": index # 当前块索引
                    }
            self._send_result(result_topic, response_data)
            index += 1
        return "文件上传成功"

    # --- 辅助方法 (保持不变) ---
    def _is_absolute_path(self, path):
        return Path(path).is_absolute()

    def _resolve_to_absolute(self, base_path, relative_path):
        return (Path(base_path) / relative_path).resolve()

    def _validate_path_in_workspace(self, target_path, workspace_path):
        try:
            Path(target_path).resolve().relative_to(Path(workspace_path).resolve())
            return True
        except ValueError:
            return False

    def _apply_patch_to_lines(self, original_lines, patch_content):
        """
        使用 unidiff 解析补丁内容，并将其应用到原始行列表。
        返回应用补丁后的行列表。
        """
        patch_set = PatchSet(patch_content)
        # 复制一份原行，以便修改
        lines = original_lines[:]
        # 偏移量：因为增删行会影响后续 hunk 的行号
        offset = 0

        for patched_file in patch_set:
            # 通常一个 diff 只涉及一个文件，直接处理所有 hunks
            for hunk in patched_file:
                # 计算在当前 lines 中的起始行（0-based）
                start = hunk.source_start - 1 + offset
                # 验证源行是否匹配 hunk 中的上下文行（可选，但推荐）
                # 获取 hunk 中非新增行的内容（上下文 + 删除行）
                source_hunk_lines = []
                for line in hunk:
                    if line.line_type != '+':   # 上下文或删除行
                        source_hunk_lines.append(line.value.rstrip('\n'))
                # 实际 lines 中的对应区域
                actual_slice = [l.rstrip('\n') for l in lines[start:start+hunk.source_length]]
                if actual_slice != source_hunk_lines:
                    # 若不匹配，尝试自动调整行号？更安全的方式是抛出异常
                    raise ValueError(f"补丁 hunk 在行 {hunk.source_start} 处不匹配上下文")

                # 构建目标行：保留上下文行，添加新增行
                new_lines_part = []
                for line in hunk:
                    if line.line_type == '-':
                        continue  # 跳过删除行
                    elif line.line_type == '+':
                        new_lines_part.append(line.value)
                    else:  # 上下文行
                        new_lines_part.append(line.value)

                # 替换原区域
                lines[start:start+hunk.source_length] = new_lines_part
                # 更新偏移量
                offset += len(new_lines_part) - hunk.source_length

        return lines

    def execute_plugin_command(self, skill_id, command, args, from_template=False):
        """
        供插件调用的同步命令执行入口
        :param skill_id: 技能ID 或 "SKILLS_WORKSPACE"
        :param command: 命令类型（如 execute_bash, read_file, write_file...）
        :param args: 参数字典
        :param from_template: 是否仅返回内容（不添加额外描述）
        :return: 命令执行结果字符串
        """

        if self.COMMAND_CHAT_COMPLETION == command:
            agent_tag = args.get(self.COMMAND_PARAM_CHAT_COMPLETION_AGENT_TAG)
            if not agent_tag:
                raise Exception("未传入代理标识 `agent_tag`")
            request = args.get(self.COMMAND_PARAM_CHAT_COMPLETION_REQUEST)
            if not request:
                raise Exception("未传入请求内容 `request`")

            try:
                url = f"{self.aifactory_url}/{self.aifactory_token}/chats/{agent_tag}/chatcompletion"

                response = requests.post(url, json=request)
                if response.status_code == 200:
                    rep = response.json()
                    choices = rep.get("choices", [])
                    if len(choices) > 0:
                        content = choices[0].get("content", "")
                        return content

                    return "请求成功，但无返回内容"
                else:
                    return f"请求失败，HTTP状态码: {response.status_code}"
            except Exception as e:
                return f"请求发生错误: {e}"





        # 确保 args 中包含 skill_id
        if 'skill_id' not in args:
            args = dict(args)  # 拷贝避免修改原字典
            args['skill_id'] = skill_id
        # 调用原有的 on_tool_call 方法，它会根据 skill_id 分发逻辑
        # 注意：on_tool_call 会抛出 Exception，我们需要捕获并返回错误信息
        try:
            result = self.on_tool_call(command, args)
            # 如果 from_template 为 True，on_tool_call 内已经处理了返回内容
            # 这里直接返回 result
            return result
        except Exception as e:
            return f"命令执行异常: {str(e)}"

    def _load_bot_plugins(self):
        """根据环境变量 BOT_PLUGINS 动态加载并启动所有机器人插件"""
        plugins_config = os.getenv('BOT_PLUGINS')
        if not plugins_config:
            logger.warning("未设置 BOT_PLUGINS 环境变量，不启动任何机器人插件")
            return

        try:
            plugins_list = json.loads(plugins_config)
        except json.JSONDecodeError as e:
            logger.error(f"解析 BOT_PLUGINS 失败: {e}")
            return

        if(len(self.bot_plugins) > 0):
            logger.warning("已启动的机器人插件将不再启动")
            return


        for cfg in plugins_list:
            plugin_type = cfg.get('type')
            if not plugin_type:
                logger.warning("插件配置缺少 'type' 字段，跳过")
                continue

            cfg = cfg.copy() # 复制一份配置，避免修改原字典
            cfg['workspace'] = str(self.skills_workspace_path) # 将工作区路径传入插件配置，插件可以通过 cfg['workspace'] 获取到技能工作区路径


            # 动态导入模块：{type}_plugin.py
            module_name = f"{plugin_type}_plugin"
            try:
                plugin_module = importlib.import_module(module_name)
            except ImportError as e:
                logger.error(f"无法导入插件模块 '{module_name}': {e}，跳过")
                continue

            # 期望的类名：首字母大写的 Type + "Plugin"，例如 "QQPlugin"
            class_name = f"{plugin_type.capitalize()}Plugin"
            if not hasattr(plugin_module, class_name):
                logger.warning(f"模块 {module_name} 中未找到类 {class_name}，跳过")
                continue

            plugin_class = getattr(plugin_module, class_name)

            # 实例化插件，传入配置和命令回调
            try:
                # 插件构造函数签名：__init__(config, command_callback)
                plugin = plugin_class(cfg, self.execute_plugin_command)
                plugin.start()
                self.bot_plugins.append(plugin)
                logger.info(f"已加载并启动机器人插件: {cfg.get('name', plugin_type)} (类型: {plugin_type})")
            except Exception as e:
                logger.error(f"启动插件 {plugin_type} 失败: {e}")

if __name__ == "__main__":
    # --- 配置项 ---
    # 实例化时传入 None，强制在 start_listening 中读取环境变量
    handler = ToolCallHandler()

    # 开始监听
    handler.start_listening()