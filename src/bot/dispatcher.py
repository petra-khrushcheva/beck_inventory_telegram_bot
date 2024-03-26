from aiogram import Dispatcher

from bot.routers.commands_router import router as command_router
from bot.routers.survey_router import router as survey_router


dp = Dispatcher()
dp.include_router(command_router)
dp.include_router(survey_router)
