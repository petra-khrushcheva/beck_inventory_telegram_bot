from aiogram import Router
from aiogram import Dispatcher
from aiogram.exceptions import TelegramForbiddenError
from aiogram.filters import Command, CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with "/start" command
    """
    pass


@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with "/help" command
    """
    pass


@router.message()
async def any_message_handler(message: Message) -> None:
    """
    This handler receives any other messages
    """
    pass
