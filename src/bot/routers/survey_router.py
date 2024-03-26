from aiogram import Router
from aiogram.types import CallbackQuery

from bot.filters.callback_data import SurveyAnswerData


router = Router()


@router.callback_query(SurveyAnswerData.filter())
async def survey_answer_handler(
    callback: CallbackQuery, callback_data: SurveyAnswerData
):
    await callback.message.answer(str(randint(1, 10)))
    # прибавить значение дата к итоговому результату
    # и переключиться на следующее состояние
