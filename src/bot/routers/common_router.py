from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def any_message_handler(message: Message) -> None:
    """
    This handler receives any other messages
    """
    pass
