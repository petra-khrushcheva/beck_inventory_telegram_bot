from aiogram import Dispatcher

from bot.routers import router


dp = Dispatcher()
dp.include_router(router)
