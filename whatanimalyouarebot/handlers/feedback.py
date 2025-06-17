from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F

router = Router()

@router.message(Command("feedback"))
async def cmd_feedback(message: types.Message):
    await message.answer(
        "💬 Оставьте ваш отзыв одним сообщением, "
        "и мы обязательно его рассмотрим!"
    )

@router.message(F.text & ~F.text.startswith('/'))
async def process_feedback(message: types.Message):
    with open("data/feedback.txt", "a") as f:
        f.write(f"{message.from_user.id}: {message.text}\n")
    await message.answer("Спасибо за ваш отзыв!")
