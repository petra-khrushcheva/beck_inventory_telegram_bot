from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from core.config import settings

storage = RedisStorage(**kwargs)  # заполнить потом

bot = Bot(token=settings.bot_token, parse_mode=ParseMode.HTML)
