from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("contact"))
async def cmd_contact(message: types.Message):
    await message.answer(
        "📞 Контакты:\n"
        "Email: example@mail.ru\n"
        "Телефон: +7 (XXX) XXX-XX-XX"
    )
