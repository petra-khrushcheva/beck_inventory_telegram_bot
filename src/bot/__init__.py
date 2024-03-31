from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis import Redis

from bot.routers import router
from core.config import settings

bot = Bot(
    token=settings.bot_token.get_secret_value(), parse_mode=ParseMode.HTML
)

redis = Redis(
    host=settings.redis_host, port=settings.redis_port, db=settings.redis_db
)
storage = RedisStorage(redis=redis)

dp = Dispatcher(storage=storage)
dp.include_router(router)
