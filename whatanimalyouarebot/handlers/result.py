from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from services.database import Database
from templates.result_texts import get_animal_description

router = Router()

@router.message(Command("result"))
async def cmd_result(message: types.Message):
    db = Database()
    user_id = message.from_user.id
    animal = db.get_user_animal(user_id)
    
    if animal:
        desc = get_animal_description(animal)
        photo_path = f"media/images/{animal.lower()}.jpg"
        
        with open(photo_path, "rb") as photo:
            await message.answer_photo(
                photo,
                caption=desc
            )
    else:
        await message.answer("Сначала пройдите тест (/start)")
