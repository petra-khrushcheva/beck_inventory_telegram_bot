from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
# from aiogram.fsm.storage.redis import RedisStorage

# from bot.routers import router
from core.config import settings

bot = Bot(token=settings.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)

# storage = RedisStorage(**kwargs)  # заполнить потом

# dp = Dispatcher(storage=storage)
# dp.include_router(router)
