from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.filters import SurveyAnswerData


def get_survey_keyboard(question: dict):
    """
    Клавиатура с вопросами теста.
    """
    builder = InlineKeyboardBuilder()
    for score, answer in question.items():
        builder.add(
            InlineKeyboardButton(
                text=answer, callback_data=SurveyAnswerData(score=score).pack()
            )
        )
    builder.adjust(1)
    return builder.as_markup()


def get_start_keyboard():
    """Клавиатура с кнопкой 'Начать тест'."""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Начать тест", callback_data="new_test"
                )
            ]
        ]
    )
