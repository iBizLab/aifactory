# wecom_plugin.py
import asyncio
import threading
import os
import re
import requests
from urllib.parse import urlparse, unquote
# qq_plugin.py
try:
    from .bot_plugin import BotPlugin  # 作为包内模块导入
except ImportError:
    from bot_plugin import BotPlugin  # 作为独立脚本导入
import uuid

try:
    from wecom_aibot_sdk import WSClient, generate_req_id
    WECOM_AVAILABLE = True
except ImportError:
    WECOM_AVAILABLE = False
    print("警告: wecom-aibot-sdk 未安装，请运行 pip install wecom-aibot-sdk")

class WecomBotClient:
    """企业微信机器人客户端（支持附件，优先使用 SDK 的 download_file）"""

    def __init__(self, plugin, bot_id: str, secret: str, loop=None):
        self.plugin = plugin
        self.bot_id = bot_id
        self.secret = secret
        self.client = None
        self.chat_session_cache = {}
        self._processed_ids = {}
        self.loop = loop
        self._running = True

        self.step_cache = {}

        # 附件下载目录
        self.download_dir = plugin.config.get("workspace", "") + "/wecom"
        os.makedirs(self.download_dir, exist_ok=True)

    async def start(self):
        if not WECOM_AVAILABLE:
            raise ImportError("wecom-aibot-sdk is required, please install: pip install wecom-aibot-sdk")

        self.client = WSClient(self.bot_id, self.secret)

        # 注册事件处理器
        self.client.on("authenticated", self._on_authenticated)
        self.client.on("message.text", self._on_text_message)
        self.client.on("message.image", self._on_image_message)
        self.client.on("message.file", self._on_file_message)
        self.client.on("event.enter_chat", self._on_enter_chat)
        self.client.on("disconnected", self._on_disconnected)

        await self.client.connect()

    async def _on_authenticated(self):
        print(f"[企业微信插件] {self.plugin.name} 认证成功")

    async def _on_disconnected(self):
        print(f"[企业微信插件] {self.plugin.name} 连接断开")

    async def _on_enter_chat(self, frame):
        welcome_msg = self.plugin.config.get("welcome_message", "你好，我是智能助手，有什么可以帮你的吗？")
        body = frame.get("body", {})
        chat_id = body.get("chatid", "")
        from_user = body.get("from", {}).get("userid", "")
        session_id = f"wecom_chat_{chat_id}_{from_user}"

        histories = self.chat_session_cache.get(session_id, [])
        histories.append({"role": "ASSISTANT", "content": welcome_msg})
        self.chat_session_cache[session_id] = histories

        stream_id = generate_req_id("welcome")
        await self.client.reply_stream(frame, stream_id, welcome_msg, finish=True)

    # ================== SDK 原生下载 ==================
    async def _download_with_sdk(self, url: str, aes_key: str, filename: str = None) -> str:
        """
        使用 wecom_aibot_sdk 的 download_file 方法下载并解密文件
        返回本地绝对路径，失败返回 None
        """

        
        try:
            result = await self.client.download_file(url, aes_key)
            if not result or not result.get("buffer"):
                print("[SDK下载] 返回数据无效")
                return None

            file_buffer = result["buffer"]
            suggested_filename = result.get("filename")

            # 确定最终文件名
            if suggested_filename:
                final_filename = suggested_filename
            elif filename:
                final_filename = filename
            else:
                parsed = urlparse(url)
                final_filename = os.path.basename(parsed.path)
                if not final_filename or '.' not in final_filename:
                    final_filename = "unnamed_file"

            # 清理不安全字符
            safe_filename = "".join(c for c in final_filename if c.isalnum() or c in "._- ").strip()
            if not safe_filename:
                safe_filename = "unnamed_file"

            # 避免重名
            save_path = os.path.join(self.download_dir, str(uuid.uuid4()))
            os.makedirs(save_path, exist_ok=True)
            save_path = os.path.join(save_path, safe_filename)

            base, ext = os.path.splitext(save_path)
            counter = 1
            while os.path.exists(save_path):
                save_path = f"{base}_{counter}{ext}"
                counter += 1

            # 写入文件
            with open(save_path, "wb") as f:
                f.write(file_buffer)

            print(f"[SDK下载成功] {save_path}")
            return os.path.abspath(save_path)

        except Exception as e:
            print(f"[SDK下载异常] {url}: {e}")
            return None

    

    # ================== 统一附件处理入口 ==================
    async def _handle_attachment_message(self, frame, msg_type: str, url: str = None, aes_key: str = None, filename: str = None):
        """
        统一处理附件消息，优先使用 SDK 下载（需提供 aes_key），否则回退到 URL 下载
        """
        body = frame.get("body", {})
        chat_id = body.get("chatid", "")
        from_user = body.get("from", {}).get("userid", "")
        msg_id = body.get("msgid", "")
        chat_type = body.get("chattype", "single")

        if msg_id in self._processed_ids:
            return
        self._processed_ids[msg_id] = None
        if len(self._processed_ids) > 1000:
            oldest = next(iter(self._processed_ids))
            del self._processed_ids[oldest]

        if chat_type == "group":
            session_id = f"wecom_group_{chat_id}_{from_user}"
        else:
            session_id = f"wecom_single_{from_user}"

        histories = self.chat_session_cache.get(session_id, [])
        histories = histories.copy()

        stream_id = generate_req_id("stream")

        
        await self.client.reply_stream(frame, stream_id, "🤔 正在处理附件...", finish=False)

        local_path = None

        # 优先使用 SDK 下载（需要 aes_key）
        if url and aes_key:
            local_path = await self._download_with_sdk(url, aes_key, filename)

        # 回退到 requests 下载
        if not local_path and url:
            loop = asyncio.get_event_loop()
            local_path = await loop.run_in_executor(None, self._download_with_requests, url, filename)

        if local_path:
            if msg_type == "image":
                user_content = f"我提供一张图片，路径在`{local_path}`"
            else:
                user_content = f"我提供一个文件，路径在`{local_path}`"
        else:
            user_content = f"[用户发送了{msg_type}，但下载失败]"

        histories.append({"role": "USER", "content": user_content})
        if len(histories) > 20:
            histories.pop(0)

        source_channel_id = stream_id + "-" + str(uuid.uuid4())

        request = {"messages": histories, "sourcechannel": source_channel_id}
        args = {"request": request, "agent_tag": self.plugin.config.get("agent_tag", "")}

        loop = asyncio.get_event_loop()
        step = {"frame": frame, "cnt": 0, "max_cnt": 3, "stream_id": stream_id, "content": ""}
        try:
            # 保存步骤缓存
            self.step_cache[source_channel_id] = step
            result = await loop.run_in_executor(
                None,
                self.plugin.command_callback,
                "SKILLS_WORKSPACE",
                "chat_completion",
                args,
                False
            )
        except Exception as e:
            result = f"处理消息时出错: {e}"
        finally:
            # 清理步骤缓存（业务回调已执行完毕，所有步骤应已发送）
            if source_channel_id in self.step_cache:
                del self.step_cache[source_channel_id]

        histories.append({"role": "ASSISTANT", "content": result})
        self.chat_session_cache[session_id] = histories

        if len(result) > 10000:
            result = result[:10000] + "\n...(内容过长，已截断)"

        last_content = step.get("content", "")
        if last_content:
            leave_length = 10000 - len(result)
            if (leave_length > 0):
                # 合入上次内容
                result = last_content[-leave_length:] + "\n" + result

        await self.client.reply_stream(frame, stream_id, result, finish=True)

    # ---------- 消息处理器 ----------
    async def _on_text_message(self, frame):
        """文本消息回调"""
        body = frame.get("body", {})
        chat_id = body.get("chatid", "")
        from_user = body.get("from", {}).get("userid", "")
        content = body.get("text", {}).get("content", "").lstrip()
        chat_type = body.get("chattype", "single")

        stream_id = generate_req_id("stream")
        if chat_type == "group":
            session_id = f"wecom_group_{chat_id}_{from_user}"
        else:
            session_id = f"wecom_single_{from_user}"

        # 忽略大小写比较命令
        if content.lower() == "/new":
            self.chat_session_cache[session_id] = []
            await self.client.reply_stream(frame, stream_id, "会话已重置", finish=True)
            return
        

        
        msg_id = body.get("msgid", "")
        if msg_id in self._processed_ids:
            return
        self._processed_ids[msg_id] = None
        if len(self._processed_ids) > 1000:
            oldest = next(iter(self._processed_ids))
            del self._processed_ids[oldest]

        histories = self.chat_session_cache.get(session_id, [])
        histories = histories.copy()
        histories.append({"role": "USER", "content": content})
        if len(histories) > 10:
            histories.pop(0)
        

        source_channel_id = stream_id + "-" + str(uuid.uuid4())

        await self.client.reply_stream(frame, stream_id, "🤔 正在思考...", finish=False)

        request = {"messages": histories, "sourcechannel": source_channel_id, "sessionid": session_id}
        args = {"request": request, "agent_tag": self.plugin.config.get("agent_tag", "")}

        step = {"frame": frame, "cnt": 0, "max_cnt": 3, "stream_id": stream_id, "content": ""}
        loop = asyncio.get_event_loop()
        try:
            # 保存步骤缓存
            self.step_cache[source_channel_id] = step
            result = await loop.run_in_executor(
                None,
                self.plugin.command_callback,
                "SKILLS_WORKSPACE",
                "chat_completion",
                args,
                False
            )
        except Exception as e:
            result = f"处理消息时出错: {e}"
        finally:
            # 清理步骤缓存（业务回调已执行完毕，所有步骤应已发送）
            if source_channel_id in self.step_cache:
                del self.step_cache[source_channel_id]

        histories.append({"role": "ASSISTANT", "content": result})
        self.chat_session_cache[session_id] = histories

        if len(result) > 10000:
            result = result[:10000] + "\n...(内容过长，已截断)"

        last_content = step.get("content", "")
        if last_content:
            leave_length = 10000 - len(result)
            if (leave_length > 0):
                # 合入上次内容
                result = last_content[-leave_length:] + "\n" + result

        await self.client.reply_stream(frame, stream_id, result, finish=True)

    async def _on_image_message(self, frame):
        """图片消息回调：提取 url 和 aeskey"""
        body = frame.get("body", {})
        image_info = body.get("image", {})
        url = image_info.get("url", "")
        aes_key = image_info.get("aeskey", "")
        await self._handle_attachment_message(frame, "image", url=url, aes_key=aes_key)

    async def _on_file_message(self, frame):
        """文件消息回调：提取 url、aeskey 和文件名"""
        body = frame.get("body", {})
        file_info = body.get("file", {})
        url = file_info.get("url", "")
        aes_key = file_info.get("aeskey", "")
        await self._handle_attachment_message(frame, "file", url=url, aes_key=aes_key)

    def output_step(self, step: dict):
        """
        向企业微信用户推送中间步骤内容。
        step 字典应包含 "source_channel"（即 stream_id）和 "content"。
        """
        # 兼容两种字段名
        source_channel = step.get("source_channel") or step.get("source_chanel")
        if not source_channel:
            return
        
        
        # 从缓存中获取上下文
        info = self.step_cache.get(source_channel)
        if not info:
            return

        frame = info["frame"]
        cnt = info["cnt"]
        max_cnt = info.get("max_cnt", 3)
        if cnt >= max_cnt:
            return

        stream_id = info.get("stream_id", source_channel.split("-")[0])

        content = step.get("content", "")
        if not content:
            return

        # 截断过长内容（可选）
        if len(content) > 10000:
            content = content[:10000] + "...(内容过长，已截断)\n"

        last_content = info.get("content", "")
        if last_content:
            leave_length = 10000 - len(content)
            if (leave_length > 0):
                # 合入上次内容
                content = last_content[-leave_length:] + "\n" + content
        info["content"] = content

        step_stream_id = generate_req_id("step")
        # 异步发送到事件循环
        asyncio.run_coroutine_threadsafe(
            self.client.reply_stream(frame, stream_id, content, finish=False),
            self.loop
        )
        info["cnt"] += 1


class WecomPlugin(BotPlugin):
    """企业微信插件（支持附件）"""

    def __init__(self, config, command_callback):
        super().__init__(config, command_callback)
        self.client = None

    def start(self):
        if not WECOM_AVAILABLE:
            raise ImportError("wecom-aibot-sdk is required, please install: pip install wecom-aibot-sdk")

        bot_id = self.config.get("bot_id", "")
        secret = self.config.get("secret", "")

        if not bot_id or not secret:
            raise ValueError("企业微信插件配置缺少 bot_id 或 secret")

        def _run():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            client = WecomBotClient(plugin=self, bot_id=bot_id, secret=secret, loop=loop)
            self.client = client
            try:
                loop.run_until_complete(client.start())
                loop.run_forever()
            except KeyboardInterrupt:
                print(f"[企业微信插件] {self.name} 收到中断信号")
            except Exception as e:
                print(f"[企业微信插件] {self.name} 运行出错: {e}")
            finally:
                loop.close()

        self.thread = threading.Thread(target=_run, daemon=True, name=f"Wecom-{self.name}")
        self.thread.start()
        print(f"[企业微信插件] {self.name} 已启动")

    def stop(self):
        print(f"[企业微信插件] {self.name} 停止")


    def output_step(self, step: dict):
        if hasattr(self, 'client') and self.client is not None:
            self.client.output_step(step)
        else:
            print(f"[企业微信插件] 警告：client 未初始化，无法输出步骤")