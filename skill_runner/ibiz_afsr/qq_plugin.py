# qq_plugin.py
import threading
import asyncio
from botpy import Client, Intents
from botpy.message import Message, DirectMessage, C2CMessage, GroupMessage
# qq_plugin.py
try:
    from .bot_plugin import BotPlugin  # 作为包内模块导入
except ImportError:
    from bot_plugin import BotPlugin  # 作为独立脚本导入
from botpy.types.message import MarkdownPayload
import os
import requests
from urllib.parse import urlparse
import uuid

class QQBotClient(Client):
    def __init__(self, plugin, loop=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plugin = plugin
        self.loop = loop or asyncio.get_event_loop()
        self.chat_session_cache = {}  # 可选：缓存用户会话信息，提升上下文连续性
        self.chat_message_cache = {}  # 聊天消息环境
        # 附件下载目录，从配置读取，默认 ./downloads/qq
        self.download_dir = plugin.config.get("workspace", "") + "/qq"
        os.makedirs(self.download_dir, exist_ok=True)

        
    async def on_ready(self):
        print(f"[QQ插件] 机器人 {self.plugin.name} 已就绪")

    async def on_at_message_create(self, message: Message):
        await self._handle_message(message.content, message, session_id="qq_at_" + message.author.id)

    async def on_direct_message_create(self, message: DirectMessage):
        await self._handle_message(message.content, message, session_id="qq_dm_" + message.author.id)

    async def on_c2c_message_create(self, message: C2CMessage):
        await self._handle_message(message.content, message, session_id="qq_c2c_" + message.author.user_openid)

    async def on_group_at_message_create(self, message: GroupMessage):
        await self._handle_message(message.content, message,
                                   session_id="qq_group_" + message.group_openid + "_" + message.author.member_openid)

    def _download_attachment(self, attachment) -> str:
        """
        下载单个附件，返回本地保存的绝对路径。
        若下载失败，返回 None。
        """
        url = attachment.url
        filename = attachment.filename if attachment.filename else os.path.basename(urlparse(url).path)
        if not url:
            return None

        # 清理文件名，移除不安全字符
        safe_filename = "".join(c for c in filename if c.isalnum() or c in "._- ").strip()
        if not safe_filename:
            safe_filename = "unnamed_file"

        # 避免重名覆盖，下载路径附加guid目录

        save_path = os.path.join(self.download_dir, str(uuid.uuid4()))
        os.makedirs(save_path, exist_ok=True)
        save_path = os.path.join(save_path, safe_filename)

        base, ext = os.path.splitext(save_path)
        counter = 1
        while os.path.exists(save_path):
            save_path = f"{base}_{counter}{ext}"
            counter += 1

        try:
            # 使用同步 requests 下载，放入线程池避免阻塞事件循环
            resp = requests.get(url, stream=True, timeout=30)
            resp.raise_for_status()
            with open(save_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            return os.path.abspath(save_path)
        except Exception as e:
            print(f"[QQ插件] 下载附件失败 {filename}: {e}")
            return None

    async def _handle_message(self, content, message, session_id):
        # 去除内容开始空格
        content = content.lstrip()

        # 忽略大小写比较命令
        if content.lower() == "/new":
            self.chat_session_cache[session_id] = []
            markdown_payload = MarkdownPayload(content="会话已重置")
            # await message.reply(markdown=markdown_payload)
            await message.reply(markdown=markdown_payload, msg_type=2)
            return

        # 获取会话记录
        histories = self.chat_session_cache.get(session_id, [])
        # 复制列表并添加当前消息
        histories = histories.copy()

        # 检查是否有附件
        attachments = getattr(message, "attachments", None)
        if attachments:
            # 处理所有附件
            saved_files = []
            for att in attachments:
                local_path = await asyncio.get_event_loop().run_in_executor(
                    None, self._download_attachment, att
                )
                if local_path:
                    saved_files.append((att.filename if att.filename else "未知文件", local_path))
            # 构建回复消息
            if saved_files:
                reply_lines = []
                reply_text = ''
                if content:
                    reply_text += f"{content}"
                else:
                    reply_text += "我提供了以下文件：\n"
                for fname, fpath in saved_files:
                    reply_lines.append(f"文件`{fname}`，存放在`{fpath}`")
                reply_text += "\n".join(reply_lines)

                content = reply_text

        histories.append({"role": "USER", "content": content})

        # 列表最大为10项，超出则删除最旧的项
        if len(histories) > 10:
            histories.pop(0)

        # 源通道标识：session_id + 随机标识
        source_channel_id = session_id + "-" + str(uuid.uuid4())

        request = {
            "messages": histories,
            "sourcechannel": source_channel_id,
            "sessionid": session_id
        }

        args = {"request": request, "agent_tag": self.plugin.config.get("agent_tag", "")}

        # 备份消息对象
        backup_message = {
            "message": message,
            "cnt": 0
        }
        self.chat_message_cache[source_channel_id] = backup_message

        # 异步执行命令（使用线程池避免阻塞事件循环）
        try:
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                None,
                self.plugin.command_callback,
                "SKILLS_WORKSPACE",  # skill_id，可改为其他技能
                "chat_completion",
                args,
                False
            )

            # 添加到列表中
            histories.append({"role": "ASSISTANT", "content": result})
            self.chat_session_cache[session_id] = histories

            # 截断过长回复
            if len(result) > 3900:
                result = result[:3900] + "\n...(内容过长，已截断)"

            markdown_payload = MarkdownPayload(content=result)
            # await message.reply(markdown=markdown_payload)
            cnt = backup_message["cnt"]
            await message.reply(markdown=markdown_payload, msg_type=2, msg_seq=str(cnt + 1))
        finally:
            # 清理缓存
            if source_channel_id in self.chat_message_cache:
                del self.chat_message_cache[source_channel_id]

    def output_step(self, step: dict):
        # source_channel = step.get("source_chanel")
        source_channel = step.get("source_channel")
        if not source_channel:
            source_channel = step.get("source_chanel")

        content = step.get("content", "")
        if source_channel and source_channel in self.chat_message_cache:
            message_info = self.chat_message_cache[source_channel]
            message = message_info["message"]
            cnt = message_info["cnt"]
            if cnt > 3:
                return
            reply_text = f"{content}"
            markdown_payload = MarkdownPayload(content=reply_text)
            # 使用客户端的循环
            asyncio.run_coroutine_threadsafe(
                message.reply(markdown=markdown_payload, msg_type=2, msg_seq=str(cnt + 1)),
                self.loop
            )
            message_info["cnt"] += 1


class QqPlugin(BotPlugin):

    def __init__(self, config, command_callback):
        super().__init__(config, command_callback)
        self.client = None

    def start(self):
        def _run():
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                intents = Intents(
                    public_guild_messages=True,
                    direct_message=True,
                    public_messages=True
                )
                client = QQBotClient(
                    plugin=self,
                    loop=loop,
                    intents=intents
                )
                self.client = client  # 保存引用
                client.run(appid=self.config['bot_id'], secret=self.config['secret'])
            finally:
                loop.close()

        self.thread = threading.Thread(target=_run, daemon=True, name=f"QQ-{self.name}")
        self.thread.start()
        print(f"[QQ插件] {self.name} 已启动")

    def stop(self):
        # botpy 没有直接停止的方法，守护线程会在主进程退出时自动结束
        try:
            self.thread.join()
            print(f"[QQ插件] {self.name} 停止")
        except Exception as e:
            print(f"[QQ插件] 停止 {self.name} 时发生错误: {e}")

    def output_step(self, step: dict):
        if self.client is None:
            return
        self.client.output_step(step)


