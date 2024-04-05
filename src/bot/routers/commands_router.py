from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards import get_start_keyboard
from bot.texts import BotText

router = Router()


async def command_answer(message: Message, text: str):
    """
    Функция отправки сообщения с кнопкой начала теста.
    Текст сообщения варьируется, кнопка нет.
    """
    await message.answer(text=text, reply_markup=get_start_keyboard())


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    """
    This handler receives messages with "/start" command.
    """
    if await state.get_state() is not None:
        await state.clear()
    await command_answer(message=message, text=BotText.START_TEXT)


@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with "/help" command.
    """
    await command_answer(message=message, text=BotText.HELP_TEXT)


@router.message(Command("cancel"))
async def command_cancel_test(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with "/cancel" command.
    """
    if await state.get_state() is not None:
        await state.clear()
    await command_answer(message=message, text=BotText.CANCEL_TEXT)
