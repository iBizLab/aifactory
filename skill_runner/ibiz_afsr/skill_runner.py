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

logger = logging.getLogger(__name__)

try:
    from unidiff import PatchSet
    UNIDIFF_AVAILABLE = True
except ImportError:
    UNIDIFF_AVAILABLE = False
    logger.warning("警告：未安装 unidiff 库，apply_patch 命令将不可用。请运行 'pip install unidiff' 安装。")


try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

MAX_EXECUTE_BASH_RETURN_CHARS = 16384

current_dir = Path(__file__).parent.resolve()
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

def replace_placeholder_path(input_str: str, place_holder: str, file_path: str) -> str:
    if input_str is None:
        return None
    pattern = re.compile(r'\{%s\}' % place_holder, re.IGNORECASE)
    result_parts = []
    last_end = 0
    for match in pattern.finditer(input_str):
        start = match.start()
        end = match.end()
        result_parts.append(input_str[last_end:start])
        if end < len(input_str):
            next_char = input_str[end]
            if next_char == '/':
                replacement = file_path + '/'
                last_end = end + 1
            elif next_char != ' ':
                replacement = file_path + '/'
                last_end = end
            else:
                replacement = file_path
                last_end = end
        else:
            replacement = file_path
            last_end = end
        result_parts.append(replacement)
    result_parts.append(input_str[last_end:])
    return ''.join(result_parts)

class ToolCallHandler:
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
    COMMAND_PARAM_EXECUTE_BASH_TIMEOUT = "timeout"
    COMMAND_PARAM_DOWNLOAD_FILE_INDEX = "index"
    COMMAND_PARAM_DOWNLOAD_FILE_SIZE = "size"
    COMMAND_PARAM_APPLY_PATCH_NEW_FILE_PATH = "new_file_path"
    COMMAND_PARAM_APPLY_PATCH_UNIFIED_DIFF = "unified_diff"
    COMMAND_PARAM_CHAT_COMPLETION_REQUEST = "request"
    COMMAND_PARAM_CHAT_COMPLETION_AGENT_TAG = "agent_tag"
    COMMAND_PARAM_OUTPUT_STEP_CONTENT = "content"
    COMMAND_PARAM_OUTPUT_STEP_REASONING_CONTENT = "reasoning_content"
    COMMAND_PARAM_OUTPUT_STEP_SOURCE_CHANNEL = "source_channel"
    COMMAND_PARAM_READ_FILE_OFFSET = "offset"
    COMMAND_PARAM_READ_FILE_LENGTH = "length"

    def __init__(self, skills_workspace_path=None, mqtt_url=None, skills_base_path=None):
        self.skills_workspace_path = Path(skills_workspace_path).resolve() if skills_workspace_path else None
        self.skills_base_path = Path(skills_base_path).resolve() if skills_base_path else None
        self.mqtt_url = mqtt_url
        self.mqtt_host = None
        self.mqtt_port = None
        self.mqtt_path = None

        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, transport="websockets")
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        self.client.on_socket_open = self._on_socket_open
        self.client.on_socket_close = self._on_socket_close
        self.client.reconnect_delay_set(min_delay=10, max_delay=60)

        self._state_lock = threading.Lock()

        self.registration_data = None
        self.aifactory_url = None
        self.aifactory_token = None

        self.is_connected = False
        self.should_stop = False
        self.is_reinitializing = False
        self.heartbeat_timer = None
        self.bot_plugins = []

        self.atexit_register = False
        self.load_bot_plugins = False
        self.heartbeat_file = Path.cwd() / ".skillrunner_heartbeat"

    def _on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            logger.info(f"已连接到MQTT WebSocket服务器 {self.mqtt_host}:{self.mqtt_port}{self.mqtt_path}")
            with self._state_lock:
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
            with self._state_lock:
                self.is_connected = False

    def _on_disconnect(self, client, userdata, flags, reason_code, properties):
        logger.warning(f"与MQTT服务器断开连接，原因码: {reason_code}")
        with self._state_lock:
            self.is_connected = False
            should_stop = self.should_stop
        if not should_stop:
            logger.warning("尝试重新连接...")

    def _on_socket_open(self, client, userdata, sock):
        logger.info("WebSocket连接已打开")

    def _on_socket_close(self, client, userdata, sock):
        logger.warning("WebSocket连接已关闭")
        with self._state_lock:
            self.is_connected = False

    def _try_send_active(self):
        def send_active_task():
            with self._state_lock:
                if self.should_stop:
                    return
                url = f"{self.aifactory_url}/{self.aifactory_token}/active"
                reg_data = self.registration_data
            if not reg_data:
                return
            current_skills = self._load_skills_manifest()
            active_payload = dict(reg_data)
            active_payload['skills'] = current_skills
            try:
                requests.post(url, json=active_payload, timeout=10)
            except Exception as e:
                logger.error(f"发送激活信号时发生错误: {e}")
        threading.Thread(target=send_active_task, daemon=True).start()

    def _start_heartbeat(self):
        with self._state_lock:
            self.should_stop = False

        def send_active():
            with self._state_lock:
                if self.should_stop:
                    return
                url = f"{self.aifactory_url}/{self.aifactory_token}/active"
                reg_data = self.registration_data
            if not reg_data:
                logger.info("触发重新初始化流程...")
                self.reinitialize()
                return

            current_skills = self._load_skills_manifest()
            active_payload = dict(reg_data)
            active_payload['skills'] = current_skills
            _next_heartbeat = False
            try:
                response = requests.post(url, json=active_payload, timeout=10)
                response_text = response.text.strip().lower()
                if response.status_code == 200:
                    if response_text == "true":
                        logger.info("成功发送激活信号 (Heartbeat)")
                        _next_heartbeat = True
                        try:
                            with open(self.heartbeat_file, 'w') as f:
                                f.write(str(time.time()))
                        except Exception as e:
                            print(f"写入心跳文件失败: {e}")
                    else:
                        logger.error(f"激活信号校验失败，服务器返回: '{response_text}' (非 true)")
                        logger.info("触发重新初始化流程...")
                        self.reinitialize()
                        return
                else:
                    logger.error(f"激活信号发送失败，HTTP状态码: {response.status_code}")
                    self.reinitialize()
                    return
            except Exception as e:
                logger.error(f"发送激活信号时发生错误: {e}")
                self.reinitialize()
                return
            finally:
                if _next_heartbeat:
                    with self._state_lock:
                        if self.heartbeat_timer:
                            self.heartbeat_timer.cancel()
                            self.heartbeat_timer = None
                        self.heartbeat_timer = threading.Timer(60.0, send_active)
                        self.heartbeat_timer.start()
                else:
                    logger.info("已停止心跳，跳过本次心跳")

        send_active()

    def reinitialize(self):
        with self._state_lock:
            if self.is_reinitializing:
                logger.warning("重入保护：当前正在进行重新初始化，忽略新的触发请求。")
                return
            self.is_reinitializing = True
            self.should_stop = True
            if self.heartbeat_timer:
                self.heartbeat_timer.cancel()
                self.heartbeat_timer = None

        logger.info("【重新初始化】流程启动...")
        try:
            self.client.disconnect()
            self.client.loop_stop(force=True)
        except:
            pass

        self._unregister_skill_runner()

        with self._state_lock:
            self.registration_data = None
            self.aifactory_url = None
            self.aifactory_token = None
            self.is_connected = False
            self.should_stop = False
            self.is_reinitializing = False
            self.heartbeat_timer = None

        logger.info("【重新初始化】清理完成，准备重启...")
        self.start_listening()

    def _load_skills_manifest(self):
        if not self.skills_base_path:
            logger.warning("警告：skills_base_path 未设置，无法加载技能清单")
            return {}
        manifest = {}
        skills_root = Path(self.skills_base_path)
        if not skills_root.exists() or not skills_root.is_dir():
            logger.warning(f"技能根目录不存在或不是目录: {skills_root}")
            return {}
        for skill_dir in skills_root.iterdir():
            if not skill_dir.is_dir():
                continue
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
        pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
        if not match:
            return None
        yaml_block = match.group(1).strip()
        if not yaml_block:
            return None
        return yaml_block

    def _register_skill_runner(self):
        try:
            with self._state_lock:
                url = f"{self.aifactory_url}/{self.aifactory_token}/register"
                workspace = str(self.skills_workspace_path)
                skills_path = str(self.skills_base_path) if self.skills_base_path else ""
            skills_manifest = self._load_skills_manifest()
            registration_data = {
                "workspace": workspace,
                "skills_path": skills_path,
                "os_type": platform.system(),
                "skills": skills_manifest
            }
            response = requests.post(url, json=registration_data, timeout=10)
            if response.status_code == 200:
                with self._state_lock:
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
        with self._state_lock:
            reg_data = self.registration_data
            aifactory_url = self.aifactory_url
            aifactory_token = self.aifactory_token
        if reg_data and aifactory_url and aifactory_token:
            try:
                url = f"{aifactory_url}/{aifactory_token}/unregister"
                response = requests.post(url, json=reg_data, timeout=10)
                if response.status_code == 200:
                    logger.info("成功发送注销信号")
                else:
                    logger.error(f"注销失败，状态码: {response.status_code}")
            except Exception as e:
                logger.error(f"注销过程中发生错误: {e}")

    def start_listening(self):
        self.aifactory_url = os.getenv('AIFACTORY_URL')
        self.aifactory_token = os.getenv('AIFACTORY_TOKEN')
        env_mqtt_url = os.getenv('AIFACTORY_MQTT')
        env_skills_base_path = os.getenv('AIFACTORY_SKILLS')
        env_skills_workspace_path = os.getenv('AIFACTORY_SKILL_WORKSPACE')

        if not self.aifactory_url or not self.aifactory_token:
            logger.error("错误：请设置环境变量 AIFACTORY_URL 和 AIFACTORY_TOKEN")
            return
        if not env_mqtt_url or not env_skills_base_path or not env_skills_workspace_path:
            logger.error("错误：请设置环境变量 AIFACTORY_MQTT, AIFACTORY_SKILLS, AIFACTORY_SKILL_WORKSPACE")
            return

        self.skills_workspace_path = Path(env_skills_workspace_path).resolve()
        self.skills_base_path = Path(env_skills_base_path).resolve()
        self.skills_workspace_path.mkdir(parents=True, exist_ok=True)

        from urllib.parse import urlparse
        parsed_url = urlparse(env_mqtt_url)
        self.mqtt_host = parsed_url.hostname
        self.mqtt_port = parsed_url.port
        self.mqtt_path = parsed_url.path or "/mqtt"

        logger.info(f"使用MQTT URL: {env_mqtt_url}")
        logger.info(f"使用Skills根目录: {self.skills_base_path}")
        logger.info(f"使用Skills工作空间: {self.skills_workspace_path}")

        while True:
            if self._register_skill_runner():
                break
            logger.error("注册失败，正在重试...")
            time.sleep(5)

        if self.atexit_register is False:
            atexit.register(self._unregister_skill_runner)
            self.atexit_register = True

        self._start_heartbeat()

        if self.load_bot_plugins is False:
            self._load_bot_plugins()
            self.load_bot_plugins = True

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
                with self._state_lock:
                    self.should_stop = True
                    if self.heartbeat_timer:
                        self.heartbeat_timer.cancel()
                        self.heartbeat_timer = None
                self._unregister_skill_runner()
                self.client.disconnect()
                logger.warning("已断开连接")
            except:
                pass

    def _on_message(self, client, userdata, msg):
        try:
            payload_str = msg.payload.decode('utf-8')
            logger.info(f"收到消息 - 主题: {msg.topic}, 载荷: {payload_str[:500]}")
            message_data = json.loads(payload_str)
            command = message_data.get('command')
            tool_call_id = message_data.get('tool_call_id')
            result_topic = message_data.get('result_topic')
            args = message_data.get('args', {})
            scope = message_data.get('scope')
            if scope:
                args["_scope"] = scope

            extended = message_data.get('extended')

            if not command:
                logger.warning("消息中缺少command字段")
                return

            skill_id = args.get(self.COMMAND_PARAM_SKILL_ID)
            if not skill_id:
                raise Exception("未传入技能标识")

            if extended is not None and not self.SKILLS_WORKSPACE == skill_id:
                skill_folder = self.skills_base_path / skill_id
                for relative_path, content in extended.items():
                    real_path = skill_folder / relative_path
                    real_path.parent.mkdir(parents=True, exist_ok=True)
                    real_path.write_text(content, encoding='utf-8')
                    logger.info(f"已写入扩展文件: {real_path.resolve()}")

            if result_topic:
                logger.info(f"工具调用ID: {tool_call_id}, 结果将发送至: {result_topic}")

            try:
                if command == self.COMMAND_UPLOAD_FILE:
                    result = self._upload_file(args, tool_call_id, result_topic)
                else:
                    result = self.on_tool_call(command, args)
                logger.info(f"工具调用结果: {result[:500]}")

                if result_topic and tool_call_id:
                    response_data = {
                        "tool_call_id": tool_call_id,
                        "result": result,
                        "error": False
                    }
                    self._send_result(result_topic, response_data)

            except Exception as e:
                error_result = f"工具调用失败: {str(e)}"
                logger.error(error_result)
                if result_topic and tool_call_id:
                    error_response = {
                        "tool_call_id": tool_call_id,
                        "result": error_result,
                        "error": True
                    }
                    self._send_result(result_topic, error_response)

        except json.JSONDecodeError:
            logger.error("消息不是有效的JSON格式")
        except Exception as e:
            logger.error(f"处理消息时发生错误: {str(e)}")

    def _send_result(self, result_topic, response_data):
        try:
            result_payload = json.dumps(response_data, ensure_ascii=False)
            self.client.publish(result_topic, result_payload)
            logger.info(f"已发送结果到主题 '{result_topic}': {result_payload[:500]}")
        except Exception as e:
            logger.error(f"发送结果失败: {str(e)}")

    def on_tool_call(self, command, args):
        skill_id = args.get(self.COMMAND_PARAM_SKILL_ID)
        if not skill_id:
            raise Exception("未传入技能标识")

        from_template = args.get(self.COMMAND_PARAM_FROM_TEMPLATE)
        if from_template:
            from_template = from_template.lower() == "true"
        else:
            from_template = False

        current_workspace_path = args.get(self.COMMAND_PARAM_WORKSPACE)
        current_workspace_dir = Path(self.skills_workspace_path).resolve()
        if current_workspace_path and len(current_workspace_path) > 0:
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


        if self.SKILLS_WORKSPACE == skill_id:
            if self.COMMAND_EXECUTE_BASH == command:
                cmd = args.get(self.COMMAND_PARAM_EXECUTE_BASH_COMMAND)
                if not cmd:
                    raise Exception("未传入执行命令")

                file_path = args.get(self.COMMAND_PARAM_WRITE_FILE_FILE_PATH)
                file_obj = None
                if file_path and len(file_path) > 0:
                    file_path = replace_placeholder_path(file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                    content = args.get(self.COMMAND_PARAM_WRITE_FILE_CONTENT, "")
                    real_path = self._is_absolute_path(file_path) and file_path or \
                        str(self._resolve_to_absolute(current_workspace_dir, file_path))
                    if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                        return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                    file_obj = Path(real_path)
                    file_obj.parent.mkdir(parents=True, exist_ok=True)
                    file_obj.write_text(content, encoding='utf-8')

                cmd = replace_placeholder_path(cmd, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))

                env = {**os.environ}
                env["SKILLS_WORKSPACE"] = str(current_workspace_dir.resolve())

                try:
                    timeout = int(args.get(self.COMMAND_PARAM_EXECUTE_BASH_TIMEOUT) or 50)
                except (ValueError, TypeError):
                    timeout = 50
                # 确保正数
                if timeout <= 0:
                    timeout = 50

                if os.name == 'nt':
                    cmd = cmd.replace("python3", "python")
                try:
                    result = subprocess.run(
                        cmd,
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=timeout,
                        cwd=str(current_workspace_dir.resolve()),
                        env=env
                    )
                    if result.returncode == 0:
                        if from_template:
                            return f"{result.stdout}"
                        if len(result.stdout) > MAX_EXECUTE_BASH_RETURN_CHARS:
                            real_ret = result.stdout[:MAX_EXECUTE_BASH_RETURN_CHARS] + "..."
                            if file_obj:
                                return f"写入文件[{file_obj.resolve()}]成功\n执行命令成功，返回以下内容（有截断）：\n{real_ret}"
                            return f"执行命令成功，返回以下内容（有截断）：\n{real_ret}"
                        else:
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
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                    return f"读取文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                file_obj = Path(real_path)
                if file_obj.exists():
                    return self._read_file_content_with_range(file_obj, args, from_template)
                else:
                    return f"读取文件发生异常，返回以下信息：\n指定文件[{file_obj.resolve()}]不存在"

            if self.COMMAND_DELETE_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                if not file_path:
                    return "删除文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
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
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                    return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                file_obj = Path(real_path)
                file_obj.parent.mkdir(parents=True, exist_ok=True)
                append = args.get(self.COMMAND_PARAM_WRITE_FILE_APPEND, False)
                if append:
                    file_obj.open('a', encoding='utf-8').write(content)
                else:
                    file_obj.write_text(content, encoding='utf-8')
                if from_template:
                    return ""
                preview_len = 50
                content_preview = content[:preview_len]
                if len(content) > preview_len:
                    content_preview += "..."
                if append:
                    return f"写入文件[{file_obj.resolve()}]成功，写入长度：{len(content)}，总长度：{file_obj.stat().st_size}, content preview: {content_preview}"
                else:
                    return f"写入文件[{file_obj.resolve()}]成功，写入长度：{len(content)}, content preview: {content_preview}"

            elif self.COMMAND_DOWNLOAD_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_WRITE_FILE_FILE_PATH)
                if not file_path:
                    return "写入文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                content = args.get(self.COMMAND_PARAM_WRITE_FILE_CONTENT, "")
                index = args.get(self.COMMAND_PARAM_DOWNLOAD_FILE_INDEX, -1)
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                    return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                file_obj = Path(real_path)
                file_obj.parent.mkdir(parents=True, exist_ok=True)
                if(index >=0):
                    if file_obj.exists() and index == 0:
                        file_obj.write_bytes(b'')
                    decoded_content = base64.b64decode(content)
                    with open(real_path, 'ab') as f:
                        f.write(decoded_content)
                    return f"OK[{index}]"
                if file_obj.exists():
                    size = args.get(self.COMMAND_PARAM_DOWNLOAD_FILE_SIZE, -1)
                    if size >= 0 and file_obj.stat().st_size != size:
                        return f"写入文件[{file_obj.resolve()}]失败，文件大小不匹配，期望: {size} bytes, 实际: {file_obj.stat().st_size} bytes"
                    return f"保存下载文件[{file_obj.resolve()}]成功"
                else:
                    return f"保存下载文件[{file_obj.resolve()}]失败"

            elif self.COMMAND_APPLY_PATCH == command:
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                new_file_path = args.get(self.COMMAND_PARAM_APPLY_PATCH_NEW_FILE_PATH)
                unified_diff = args.get(self.COMMAND_PARAM_APPLY_PATCH_UNIFIED_DIFF)
                if not file_path:
                    return "应用补丁发生异常，返回以下信息：\n未传入应用文件路径 `file_path`"
                if not new_file_path:
                    return "应用补丁发生异常，返回以下信息：\n未传入写入文件路径 `new_file_path`"
                if not unified_diff:
                    return "应用补丁发生异常，返回以下信息：\n未传入补丁内容 `unified_diff`"
                file_path = replace_placeholder_path(file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                new_file_path = replace_placeholder_path(new_file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                real_file_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
                if not self._validate_path_in_workspace(real_file_path, current_workspace_dir):
                    return f"应用补丁发生异常，返回以下信息：\n应用文件实际路径 [{real_file_path}] 不在工作区中，禁止访问！"
                file_obj = Path(real_file_path)
                if not file_obj.exists():
                    return f"应用补丁发生异常，返回以下信息：\n应用文件 [{file_obj.resolve()}] 不存在！"
                real_new_path = self._is_absolute_path(new_file_path) and new_file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, new_file_path))
                if not self._validate_path_in_workspace(real_new_path, current_workspace_dir):
                    return f"应用补丁发生异常，返回以下信息：\n写入文件实际路径 [{real_new_path}] 不在工作区中，禁止访问！"
                new_file_obj = Path(real_new_path)
                new_file_obj.parent.mkdir(parents=True, exist_ok=True)
                if not UNIDIFF_AVAILABLE:
                    return "应用补丁失败：未安装 unidiff 库，请执行 'pip install unidiff' 后重试。"
                try:
                    with open(file_obj, 'r', encoding='utf-8') as f:
                        original_lines = f.readlines()
                    patched_lines = self._apply_patch_to_lines(original_lines, unified_diff)
                    with open(new_file_obj, 'w', encoding='utf-8') as f:
                        f.writelines(patched_lines)
                    if from_template:
                        return ""
                    return f"应用补丁写入文件 [{new_file_obj.resolve()}] 成功"
                except Exception as e:
                    return f"应用补丁发生异常：{str(e)}"
            elif self.COMMAND_OUTPUT_STEP == command:
                # 遍历插件时复制列表，避免长时间持有锁
                with self._state_lock:
                    plugins_copy = self.bot_plugins[:]
                for plugin in plugins_copy:
                    try:
                        plugin.output_step(args)
                    except Exception as e:
                        logger.error(f"插件 {plugin.__class__.__name__} 在 output_step 中发生异常: {e}")
                if from_template:
                    return ""
                return "成功"

        else:
            skill_folder = self.skills_base_path / skill_id

            if self.COMMAND_EXECUTE_BASH == command:
                cmd = args.get(self.COMMAND_PARAM_EXECUTE_BASH_COMMAND)
                if not cmd:
                    raise Exception("未传入执行命令")
                env = args.get(self.COMMAND_PARAM_EXECUTE_BASH_ENV)
                if not env:
                    env = {}
                env = {**os.environ, **env}
                env["SKILLS_WORKSPACE"] = str(current_workspace_dir.resolve())
                env["SKILL_BASEDIR"] = str(skill_folder.resolve())

                file_obj = None
                file_path = args.get(self.COMMAND_PARAM_WRITE_FILE_FILE_PATH)
                if file_path and len(file_path) > 0:
                    file_path = replace_placeholder_path(file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                    content = args.get(self.COMMAND_PARAM_WRITE_FILE_CONTENT, "")
                    real_path = self._is_absolute_path(file_path) and file_path or \
                        str(self._resolve_to_absolute(current_workspace_dir, file_path))
                    if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                        return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！"
                    file_obj = Path(real_path)
                    file_obj.parent.mkdir(parents=True, exist_ok=True)
                    file_obj.write_text(content, encoding='utf-8')
                cmd = replace_placeholder_path(cmd, "baseDir", str(skill_folder.resolve()))
                cmd = replace_placeholder_path(cmd, "SKILL_BASEDIR", str(skill_folder.resolve()))
                cmd = replace_placeholder_path(cmd, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))

                try:
                    timeout = int(args.get(self.COMMAND_PARAM_EXECUTE_BASH_TIMEOUT) or 50)
                except (ValueError, TypeError):
                    timeout = 50
                # 确保正数
                if timeout <= 0:
                    timeout = 50

                if os.name == 'nt':
                    cmd = cmd.replace("python3", "python")
                try:
                    result = subprocess.run(
                        cmd,
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=timeout,
                        cwd=str(skill_folder.resolve()),
                        env=env
                    )
                    if result.returncode == 0:
                        if from_template:
                            return f"{result.stdout}"
                        if len(result.stdout) > MAX_EXECUTE_BASH_RETURN_CHARS:
                            real_ret = result.stdout[:MAX_EXECUTE_BASH_RETURN_CHARS] + "..."
                            if file_obj:
                                return f"写入文件[{file_obj.resolve()}]成功\n执行命令成功，返回以下内容（有截断）：\n{real_ret}"
                            return f"执行命令成功，返回以下内容（有截断）：\n{real_ret}"
                        else:
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
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(skill_folder, file_path))
                if not self._validate_path_in_workspace(real_path, skill_folder):
                    return f"读取文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在技能目录中，禁止访问！"
                file_obj = Path(real_path)
                if file_obj.exists():
                    return self._read_file_content_with_range(file_obj, args, from_template)
                else:
                    return f"读取文件发生异常，返回以下信息：\n指定文件[{file_obj.resolve()}]不存在"

            elif self.COMMAND_DELETE_FILE == command:
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                if not file_path:
                    return "删除文件发生异常，返回以下信息：\n未传入文件路径`file_path`"
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(skill_folder, file_path))
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
                real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(skill_folder, file_path))
                if not self._validate_path_in_workspace(real_path, skill_folder):
                    return f"写入文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在技能目录中，禁止访问！"
                file_obj = Path(real_path)
                file_obj.parent.mkdir(parents=True, exist_ok=True)
                append = args.get(self.COMMAND_PARAM_WRITE_FILE_APPEND, False)
                if append:
                    file_obj.open('a', encoding='utf-8').write(content)
                else:
                    file_obj.write_text(content, encoding='utf-8')
                if file_path == "SKILL.md":
                    self._try_send_active()
                if from_template:
                    return ""
                preview_len = 50
                content_preview = content[:preview_len]
                if len(content) > preview_len:
                    content_preview += "..."
                if append:
                    return f"写入文件[{file_obj.resolve()}]成功，写入长度：{len(content)}，总长度：{file_obj.stat().st_size}, content preview: {content_preview}"
                else:
                    return f"写入文件[{file_obj.resolve()}]成功，写入长度：{len(content)}, content preview: {content_preview}"
            elif self.COMMAND_APPLY_PATCH == command:
                file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
                new_file_path = args.get(self.COMMAND_PARAM_APPLY_PATCH_NEW_FILE_PATH)
                unified_diff = args.get(self.COMMAND_PARAM_APPLY_PATCH_UNIFIED_DIFF)
                if not file_path:
                    return "应用补丁发生异常，返回以下信息：\n未传入应用文件路径 `file_path`"
                if not new_file_path:
                    return "应用补丁发生异常，返回以下信息：\n未传入写入文件路径 `new_file_path`"
                if not unified_diff:
                    return "应用补丁发生异常，返回以下信息：\n未传入补丁内容 `unified_diff`"
                file_path = replace_placeholder_path(file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                new_file_path = replace_placeholder_path(new_file_path, "SKILLS_WORKSPACE", str(current_workspace_dir.resolve()))
                real_file_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(skill_folder, file_path))
                if not self._validate_path_in_workspace(real_file_path, skill_folder):
                    return f"应用补丁发生异常，返回以下信息：\n应用文件实际路径 [{real_file_path}] 不在技能目录中，禁止访问！"
                file_obj = Path(real_file_path)
                if not file_obj.exists():
                    return f"应用补丁发生异常，返回以下信息：\n应用文件 [{file_obj.resolve()}] 不存在！"
                real_new_path = self._is_absolute_path(new_file_path) and new_file_path or \
                    str(self._resolve_to_absolute(skill_folder, new_file_path))
                if not self._validate_path_in_workspace(real_new_path, skill_folder):
                    return f"应用补丁发生异常，返回以下信息：\n写入文件实际路径 [{real_new_path}] 不在技能目录中，禁止访问！"
                new_file_obj = Path(real_new_path)
                new_file_obj.parent.mkdir(parents=True, exist_ok=True)
                if not UNIDIFF_AVAILABLE:
                    return "应用补丁失败：未安装 unidiff 库，请执行 'pip install unidiff' 后重试。"
                try:
                    with open(file_obj, 'r', encoding='utf-8') as f:
                        original_lines = f.readlines()
                    patched_lines = self._apply_patch_to_lines(original_lines, unified_diff)
                    with open(new_file_obj, 'w', encoding='utf-8') as f:
                        f.writelines(patched_lines)
                    if from_template:
                        return ""
                    return f"应用补丁写入文件 [{new_file_obj.resolve()}] 成功"
                except Exception as e:
                    return f"应用补丁发生异常：{str(e)}"

        raise Exception(f"未支持的指令[{command}]")

    def _upload_file(self, args, tool_call_id, result_topic):
        skill_id = args.get(self.COMMAND_PARAM_SKILL_ID)
        if not skill_id:
            raise Exception("未传入技能标识")
        file_path = args.get(self.COMMAND_PARAM_READ_FILE_FILE_PATH)
        if not file_path:
            raise Exception("读取文件发生异常，返回以下信息：\n未传入文件路径`file_path`")

        current_workspace_path = args.get(self.COMMAND_PARAM_WORKSPACE)
        current_workspace_dir = Path(self.skills_workspace_path).resolve()
        if current_workspace_path and len(current_workspace_path) > 0:
            current_workspace_dir = Path(current_workspace_path).resolve()
            current_workspace_dir.mkdir(parents=True, exist_ok=True)
        else:
            current_workspace_path = str(self.skills_workspace_path.resolve())

        if self.SKILLS_WORKSPACE == skill_id:
            real_path = self._is_absolute_path(file_path) and file_path or \
                    str(self._resolve_to_absolute(current_workspace_dir, file_path))
            if not self._validate_path_in_workspace(real_path, current_workspace_dir):
                raise Exception(f"读取文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在工作区中，禁止访问！")
        else:
            skill_folder = self.skills_base_path / skill_id
            real_path = self._is_absolute_path(file_path) and file_path or \
                str(self._resolve_to_absolute(skill_folder, file_path))
            if not self._validate_path_in_workspace(real_path, skill_folder):
                raise Exception(f"读取文件发生异常，返回以下信息：\n文件实际路径[{real_path}]不在[{skill_id}]工作区中，禁止访问！")

        file_obj = Path(real_path)
        if not file_obj.exists():
            raise Exception(f"文件不存在: {real_path}")

        data = file_obj.read_bytes()
        chunk_size = 64 * 1024
        index = 0
        for i in range(0, len(data), chunk_size):
            chunk = data[i : i + chunk_size]
            response_data = {
                "tool_call_id": tool_call_id,
                "result": base64.b64encode(chunk).decode('utf-8'),
                "error": False,
                "index": index
            }
            self._send_result(result_topic, response_data)
            index += 1
        return "文件上传成功"

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
        patch_set = PatchSet(patch_content)
        lines = original_lines[:]
        offset = 0
        for patched_file in patch_set:
            for hunk in patched_file:
                start = hunk.source_start - 1 + offset
                source_hunk_lines = []
                for line in hunk:
                    if line.line_type != '+':
                        source_hunk_lines.append(line.value.rstrip('\n'))
                actual_slice = [l.rstrip('\n') for l in lines[start:start+hunk.source_length]]
                if actual_slice != source_hunk_lines:
                    raise ValueError(f"补丁 hunk 在行 {hunk.source_start} 处不匹配上下文")
                new_lines_part = []
                for line in hunk:
                    if line.line_type == '-':
                        continue
                    elif line.line_type == '+':
                        new_lines_part.append(line.value)
                    else:
                        new_lines_part.append(line.value)
                lines[start:start+hunk.source_length] = new_lines_part
                offset += len(new_lines_part) - hunk.source_length
        return lines

    def _parse_int_arg(self, value, default=-1):
        try:
            if value is None:
                return default
            return int(value)
        except (ValueError, TypeError):
            return default

    def _read_file_content_with_range(self, file_obj, args, from_template):
        content = file_obj.read_text(encoding='utf-8')

        offset = self._parse_int_arg(args.get(self.COMMAND_PARAM_READ_FILE_OFFSET), -1)
        length = self._parse_int_arg(args.get(self.COMMAND_PARAM_READ_FILE_LENGTH), -1)

        offset_mode = 0
        if offset >= 0 or length >= 0:
            total_length = len(content)
            start = offset if offset >= 0 else 0

            if start >= total_length:
                content = ""
                offset_mode = 2
            else:
                max_length = length if length >= 0 else total_length - start
                end = min(start + max_length, total_length)
                content = content[start:end]
                offset = start
                length = end - start
                offset_mode = 1

        if from_template:
            return content

        if offset_mode == 1:
            return f"读取文件成功[offset:{offset}, length:{length}, total:{total_length}]，内容如下：\n{content}"
        if offset_mode == 2:
            return "读取文件失败，起始位置`offset`已超出文件内容长度"
        return f"读取文件成功，内容如下：\n{content}"


    def execute_plugin_command(self, skill_id, command, args, from_template=False):
        if self.COMMAND_CHAT_COMPLETION == command:
            agent_tag = args.get(self.COMMAND_PARAM_CHAT_COMPLETION_AGENT_TAG)
            if not agent_tag:
                raise Exception("未传入代理标识 `agent_tag`")
            request = args.get(self.COMMAND_PARAM_CHAT_COMPLETION_REQUEST)
            if not request:
                raise Exception("未传入请求内容 `request`")
            try:
                with self._state_lock:
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

        if 'skill_id' not in args:
            args = dict(args)
            args['skill_id'] = skill_id
        try:
            result = self.on_tool_call(command, args)
            return result
        except Exception as e:
            return f"命令执行异常: {str(e)}"

    def _load_bot_plugins(self):
        plugins_config = os.getenv('BOT_PLUGINS')
        if not plugins_config:
            logger.warning("未设置 BOT_PLUGINS 环境变量，不启动任何机器人插件")
            return
        try:
            plugins_list = json.loads(plugins_config)
        except json.JSONDecodeError as e:
            logger.error(f"解析 BOT_PLUGINS 失败: {e}")
            return

        with self._state_lock:
            if len(self.bot_plugins) > 0:
                logger.warning("已启动的机器人插件将不再启动")
                return

        for cfg in plugins_list:
            plugin_type = cfg.get('type')
            if not plugin_type:
                logger.warning("插件配置缺少 'type' 字段，跳过")
                continue
            cfg = cfg.copy()
            cfg['workspace'] = str(self.skills_workspace_path)
            module_name = f"{plugin_type}_plugin"
            try:
                plugin_module = importlib.import_module(module_name)
            except ImportError as e:
                logger.error(f"无法导入插件模块 '{module_name}': {e}，跳过")
                continue
            class_name = f"{plugin_type.capitalize()}Plugin"
            if not hasattr(plugin_module, class_name):
                logger.warning(f"模块 {module_name} 中未找到类 {class_name}，跳过")
                continue
            plugin_class = getattr(plugin_module, class_name)
            try:
                plugin = plugin_class(cfg, self.execute_plugin_command)
                plugin.start()
                with self._state_lock:
                    self.bot_plugins.append(plugin)
                logger.info(f"已加载并启动机器人插件: {cfg.get('name', plugin_type)} (类型: {plugin_type})")
            except Exception as e:
                logger.error(f"启动插件 {plugin_type} 失败: {e}")

if __name__ == "__main__":
    handler = ToolCallHandler()
    handler.start_listening()