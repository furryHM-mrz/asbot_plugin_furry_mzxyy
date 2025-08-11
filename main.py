import asyncio
import aiohttp
import logging
import random
import os
from astrbot.api.all import AstrMessageEvent, CommandResult
from astrbot.api.star import register, Star
import astrbot.api.event.filter as filter

logger = logging.getLogger("astrbot")


@register("asbot_plugin_furry_mzxyy", "furryhm", "毛主席一言", "1.0.0")
class Main(Star):
    def __init__(self, context=None) -> None:
        super().__init__(context)
        # 加载本地词库
        self.quotes = []
        # 获取插件目录
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        quotes_file = os.path.join(plugin_dir, "quotes.txt")
        try:
            with open(quotes_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        self.quotes.append(line)
        except FileNotFoundError:
            logger.error("本地词库文件未找到")
            self.quotes = ["默认毛主席语录 —— 毛泽东"]

    @filter.command("毛主席一言")
    async def hitokoto(self, message: AstrMessageEvent):
        """来一条毛主席一言"""
        if not self.quotes:
            return CommandResult().error("词库为空")
        
        # 随机选择一条语录
        quote = random.choice(self.quotes)
        return CommandResult().message(quote)