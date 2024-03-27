import json
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import State

from bot.filters.callback_data import SurveyAnswerData
from bot.filters.states import SurveyState
from bot.keyboards import get_survey_keyboard
from bot.utils import get_test_result


router = Router()


QUESTION_TEXT = (
    "Что лучше описывает ваше состояние за прошедшую неделю и сегодня?"
)


with open(
    "src/bot/survey_questions.json"
) as file:  # сюда добавить асинхронность
    questions = json.load(file)

for i in range(len(questions)):
    pass


@router.callback_query(F.data == "new_test")
@router.message(Command("new_test"))
async def new_test_handler(query: Message | CallbackQuery, state: FSMContext):
    """
    This handler receives "new_test" command or callback
    and answers with first question of the test
    """
    chat_id = (
        query.chat.id if isinstance(query, Message) else query.message.chat.id
    )
    await query.bot.send_message(
        chat_id=chat_id,
        text=QUESTION_TEXT,
        reply_markup=await get_survey_keyboard(question=questions[0]),
    )
    await state.set_data({})
    await state.set_state(State(state="question1"))


# last callback answer
@router.callback_query(SurveyState.question21, SurveyAnswerData.filter())
async def last_answer_handler(
    callback: CallbackQuery, callback_data: SurveyAnswerData, state: FSMContext
):
    await state.update_data(
        score=int(callback_data.value)
    )  # прибавить значение дата к итоговому результату???????
    user_data = state.get_data()
    await callback.message.answer(
        text=get_test_result(
            score=f"что-то полученное из юзер даты{user_data}"
        )
    )
    await state.clear()


@router.callback_query(
    StateFilter(State(state="question1")),
    SurveyAnswerData.filter(),  # написать фильр для стейт
)
async def survey_answer_handler(
    callback: CallbackQuery, callback_data: SurveyAnswerData, state: FSMContext
):
    question_number = int((await state.get_state()).replace("question", ""))
    await state.update_data(score=callback_data.value)
    await callback.message.edit_reply_markup(
        text=QUESTION_TEXT,
        reply_markup=get_survey_keyboard(question=questions[question_number]),
    )
    await state.set_state(State(state=f"question{question_number+1}"))


# и так 20-21 раз
...
