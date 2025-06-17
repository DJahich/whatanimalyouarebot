from aiogram import Router
from aiogram.filters import CommandStart

from handlers.start import router as start_router
from handlers.contact import router as contact_router
from handlers.feedback import router as feedback_router
from handlers.result import router as result_router
from handlers.sharing import router as share_router

router = Router(name="MainRouter")

router.include_router(start_router)
router.include_router(contact_router)
router.include_router(feedback_router)
router.include_router(result_router)
router.include_router(share_router)

@router.message(CommandStart())
async def universal_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Добро пожаловать! Используйте /start для начала.")

@router.errors()
async def error_handler(event: ErrorEvent):
    """Глобальный обработчик ошибок"""
    logger.error(f"Ошибка в обработчике: {event.exception}")
    await event.update.message.answer("⚠️ Произошла ошибка. Попробуйте позже.")
