import json
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State

from bot.filters.callback_data import SurveyAnswerData
from bot.filters.states import SurveyState
from bot.keyboards import get_keyboard


router = Router()


QUESTION_TEXT = (
    "Что лучше описывает ваше состояние за прошедшую неделю и сегодня?"
)


async def get_test_result(score) -> str:
    pass


with open(
    "bot/survey_questions.json", "r"
) as file:  # сюда добавить асинхронность
    questions = json.load(file)


for i in range(len(questions)):
    pass
# здесб функция регистрации роутеров один за другим


# возможно здесь стоит поставить не команду а коллбэк кнопку
# (или коллбэк кнопку с командой)
@router.message(Command("new_test"))
async def new_test_handler(message: Message, state: FSMContext):
    await message.answer(
        text=QUESTION_TEXT,
        reply_markup=get_keyboard(question=questions[0]),
    )
    await state.set_state(SurveyState.question1)


@router.callback_query(
    State(state="question1", group_name="SurveyState"),  # поэкспериментировать с таким подходом на простом боте
    SurveyAnswerData.filter(),
)
# затем посмотреть регистрацию ботов через функцию, а не через декоратор

async def survey_answer1_handler(
    callback: CallbackQuery, callback_data: SurveyAnswerData, state: FSMContext
):
    await state.update_data(score=int(callback_data.value))
    await callback.message.edit_reply_markup(
        text=QUESTION_TEXT, reply_markup=get_keyboard(question=questions[1])
    )
    await state.set_state(SurveyState.question2)


# и так 20-21 раз
...


# last callback answer
@router.callback_query(SurveyState.question21, SurveyAnswerData.filter())
async def survey_answer21_handler(
    callback: CallbackQuery, callback_data: SurveyAnswerData, state: FSMContext
):
    await state.update_data(
        answer21=int(callback_data.value)
    )  # прибавить значение дата к итоговому результату???????
    user_data = state.get_data()
    await callback.message.answer(
        text=get_test_result(
            score=f"что-то полученное из юзер даты{user_data}"
        )
    )
    await state.clear()
