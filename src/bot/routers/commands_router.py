from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from bot.keyboards import get_start_keyboard


router = Router()

START_TEXT = (
    "Вам будет предложен ряд утверждений.\n\nВыберите одно "
    "утверждение в каждой группе, которое лучше всего описывает "
    "ваше состояние "
    f"{hbold('за прошедшую неделю, включая сегодняшний день')}.\n\n"
    "Прежде чем сделать свой выбор, внимательно прочтите все "
    "утверждения в каждой группе."
)

HELP_TEXT = (
    "Здесь вы можете пройти тест Бека для определения депрессии.\n\n"
    "Пожалуйста, обратите внимание на то что онлайн-тест не может "
    "быть использован для самостоятельной постановки диагноза.\n\n"
    "В случае любых сомнений обращайтесь к квалифицированным специалистам."
)


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    """
    This handler receives messages with "/start" command
    """
    if await state.get_state() is not None:
        await state.clear()
    await message.answer(
        text=START_TEXT, reply_markup=await get_start_keyboard()
    )


@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with "/help" command
    """
    await message.answer(
        text=HELP_TEXT, reply_markup=await get_start_keyboard()
    )
