from aiogram import Router, F
from aiogram.types import Message

from keyboards.all_keyboards import main_keyboard

admin_router = Router()

@admin_router.message(F.text == "Админ панель")
async def cmd(message: Message):
    await message.answer(str(message.from_user.id), reply_markup=main_keyboard(message.from_user.id))