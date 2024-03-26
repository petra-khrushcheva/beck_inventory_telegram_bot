from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from bot.filters.callback_data import SurveyAnswerData


async def get_keyboard(question: dict):
    builder = InlineKeyboardBuilder()
    for score, answer in question.items():
        builder.add(
            InlineKeyboardButton(
                text=answer, callback_data=SurveyAnswerData(value=score)
            )
        )
    builder.adjust(1)
    return builder.as_markup()
