# ibiz_afsr/__init__.py
"""
iBizLab AI Factory Skill Runner
Lightweight edge agent for executing AI Skills locally with secure cloud-edge collaboration.
"""

from .bot_plugin import BotPlugin
from .qq_plugin import QqPlugin
from .skill_runner import ToolCallHandler
from .wecom_plugin import WecomPlugin
from .main import main

__version__ = "1.0.0"
__author__ = "iBizLab"

__all__ = [
    "BotPlugin",
    "QqPlugin",
    "ToolCallHandler",
    "WecomPlugin",
    "main",
]