from aiogram.filters.callback_data import CallbackData


class SurveyAnswerData(CallbackData, prefix="answer"):
    score: int
