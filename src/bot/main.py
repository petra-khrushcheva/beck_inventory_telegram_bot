from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from bot.routers import router
from core.config import settings

storage = RedisStorage(**kwargs)  # заполнить потом

bot = Bot(token=settings.bot_token, parse_mode=ParseMode.HTML)

dp = Dispatcher()
dp.include_router(router)
