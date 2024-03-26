from aiogram import Router

from bot.routers.commands_router import router as command_router
from bot.routers.survey_router import router as survey_router

router = Router()
router.include_routers(command_router, survey_router)
