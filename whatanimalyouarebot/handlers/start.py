from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from templates.intro import WELCOME_MESSAGE
from services.database import Database

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    db = Database()
    user_id = message.from_user.id
    
    if not db.user_exists(user_id):
        db.add_user(user_id, message.from_user.full_name)
    
    await message.answer(
        WELCOME_MESSAGE,
        parse_mode="Markdown"
    )
    await message.answer("Начнем тест! Ответьте на несколько вопросов.")
