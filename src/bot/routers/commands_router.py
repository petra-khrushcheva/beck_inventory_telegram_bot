from typing import Optional
from aiogram import F, Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from bot.keyboards import get_start_keyboard


router = Router()

START_TEXT = ("Вам будет предложен ряд утверждений.\n\nВыберите одно "
              "утверждение в каждой группе, которое лучше всего описывает "
              "ваше состояние "
              f"{hbold('за прошедшую неделю, включая сегодняшний день')}.\n\n"
              "Прежде чем сделать свой выбор, внимательно прочтите все "
              "утверждения в каждой группе.")


async def start_new_test(query)



@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    """
    This handler receives messages with "/start" command
    """
    if await state.get_state() is not None:
        await state.clear()
    await message.answer(
        text=START_TEXT,
        reply_markup=await get_start_keyboard()
    )


async def new_test_handler(query):
    pass
# здесь код который отправляет первый вопрос теста


router.callback_query.register(new_test_handler, F.data == "new_test")
router.message.register(new_test_handler, Command("new_test"))






@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text='Этот бот демонстрирует работу FSM\n\n'
             'Чтобы перейти к заполнению анкеты - '
             'отправьте команду /fillform'
    )


@router.message(CommandStart())
async def command_start_handler_(message: Message, state: FSMContext) -> None:
    """
    This handler receives messages with "/start" command
    """
    await state.clear()
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
