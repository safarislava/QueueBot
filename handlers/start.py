from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.all_keyboards import main_keyboard

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Бот начал работу', reply_markup=main_keyboard(message.from_user.id))
    await message.answer(str(message.from_user.id), reply_markup=main_keyboard(message.from_user.id))

