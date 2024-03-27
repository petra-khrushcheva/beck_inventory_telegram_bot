from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.filters.callback_data import SurveyAnswerData


async def get_survey_keyboard(question: dict):
    builder = InlineKeyboardBuilder()
    for score, answer in question.items():
        builder.add(
            InlineKeyboardButton(
                text=answer, callback_data=SurveyAnswerData(value=score)
            )
        )
    builder.adjust(1)
    return builder.as_markup()


async def get_start_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Начать тест", callback_data="new_test"
                )
            ]
        ]
    )
    return keyboard
