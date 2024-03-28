import json
import pathlib

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import CallbackQuery, Message

from bot.filters.callback_data import SurveyAnswerData
from bot.keyboards import get_survey_keyboard
from bot.texts.texts import BotText
from bot.utils import get_test_result

router = Router()

with open(
    f"{pathlib.Path(__file__).parents[1]}/texts/survey_questions.json"
) as file:
    questions = json.load(file)


number_of_questions = len(questions)


@router.callback_query(F.data == "new_test")
@router.message(Command("new_test"))
async def new_test_handler(query: Message | CallbackQuery, state: FSMContext):
    """
    This handler receives "new_test" command or callback
    and replies with first question of the test.
    """
    chat_id = (
        query.chat.id if isinstance(query, Message) else query.message.chat.id
    )
    await query.bot.send_message(
        chat_id=chat_id,
        text=BotText.QUESTION_TEXT,
        reply_markup=get_survey_keyboard(question=questions[0]),
    )
    await state.set_data({})
    await state.set_state(State(state="question1"))


@router.callback_query(
    State(state=f"question{number_of_questions}"),
    SurveyAnswerData.filter(),
)
async def last_answer_handler(
    callback: CallbackQuery, callback_data: SurveyAnswerData, state: FSMContext
):
    """
    This handler receives the last test answer
    and replies with the test result.
    """
    await state.update_data(
        data={f"answer{number_of_questions}": callback_data.score}
    )
    user_data: dict = await state.get_data()
    score = sum([value for value in user_data.values()])
    await callback.message.edit_text(
        text=BotText.RESULT_TEXT + get_test_result(score=score)
    )
    await state.clear()


@router.callback_query(
    State(F.state.startswith("question")),
    SurveyAnswerData.filter(),
)
async def survey_answer_handler(
    callback: CallbackQuery, callback_data: SurveyAnswerData, state: FSMContext
):
    """
    This handler recieves all test answers except for the last one
    and replies with the next question.
    """
    question_number = int((await state.get_state()).replace("@:question", ""))
    await state.update_data(
        data={f"answer{question_number}": callback_data.score}
    )
    await callback.message.edit_reply_markup(
        reply_markup=get_survey_keyboard(question=questions[question_number]),
    )
    await state.set_state(State(state=f"question{question_number+1}"))
