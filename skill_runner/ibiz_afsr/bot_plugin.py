# bot_plugin.py
from abc import ABC, abstractmethod

class BotPlugin(ABC):
    """机器人插件抽象基类"""
    
    def __init__(self, config: dict, command_callback):
        """
        :param config: 插件配置（从环境变量读取的 JSON 对象）
        :param command_callback: 命令执行回调函数，签名: (skill_id, command, args, from_template) -> str
        """
        self.config = config
        self.command_callback = command_callback
        self.name = config.get('name', self.__class__.__name__)
        
    @abstractmethod
    def start(self):
        """启动插件（通常创建新线程）"""
        pass
    
    @abstractmethod
    def stop(self):
        """停止插件，释放资源"""
        pass
    
    @abstractmethod
    def output_step(self, step: dict):
        """输出步骤"""
        pass