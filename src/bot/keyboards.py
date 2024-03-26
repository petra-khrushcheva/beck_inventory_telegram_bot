from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from bot.filters.callback_data import SurveyAnswerData


async def get_keyboard(question: dict):
    builder = InlineKeyboardBuilder()
    for key, value in question.items():
        builder.add(
            InlineKeyboardButton(
                text=value, callback_data=SurveyAnswerData(value=key)
            )
        )
    builder.adjust(1)
    return builder.as_markup()
