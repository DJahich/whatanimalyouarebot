from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.database import Database

router = Router()

@router.message(Command("share"))
async def cmd_share(message: types.Message):
    db = Database()
    user_id = message.from_user.id
    animal = db.get_user_animal(user_id)
    
    if animal:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="Поделиться результатом",
                switch_inline_query=f"Моё животное - {animal}")
            ]
        ])
        await message.answer(
            f"Ваше животное: {animal}",
            reply_markup=keyboard
        )
    else:
        await message.answer("Сначала пройдите тест (/start)")
