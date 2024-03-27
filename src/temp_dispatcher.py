from typing import Optional
from aiogram import F, Dispatcher
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.utils.markdown import hbold
from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


dp = Dispatcher()


from bot.keyboards import get_start_keyboard


START_TEXT = ("Вам будет предложен ряд утверждений.\n\nВыберите одно "
              "утверждение в каждой группе, которое лучше всего описывает "
              "ваше состояние "
              f"{hbold('за прошедшую неделю, включая сегодняшний день')}.\n\n"
              "Прежде чем сделать свой выбор, внимательно прочтите все "
              "утверждения в каждой группе."
              "Начать тест: /new_test")


@dp.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    if await state.get_state() is not None:
        await state.clear()
    await message.answer(
        text=START_TEXT,
        reply_markup=await get_start_keyboard()
    )


async def another_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Другая клава", callback_data="some_data"
                )
            ]
        ]
    )
    return keyboard


@dp.callback_query(F.data == "new_test")
@dp.message(Command("new_test"))
async def new_test_handler(query: Message | CallbackQuery, state: FSMContext):
    chat_id = query.chat.id if isinstance(query, Message) else query.message.chat.id
    await query.bot.send_message(chat_id=chat_id, text=f"Это наш чат айди: {chat_id}", reply_markup=await another_keyboard())
