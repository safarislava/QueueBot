from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from controllers.user import user_controller
from entity.state import Registration
from entity.user import User
from keyboards.all_keyboards import main_keyboard

start_router = Router()

@start_router.message(StateFilter(None), CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    await message.answer("Бот начал работу")
    await message.answer(str(message.from_user.id))
    await message.answer("Введи своё имя")
    await state.set_state(Registration.registration)

@start_router.message(Registration.registration)
async def registration(message: Message, state: FSMContext) -> None:
    # print(message.from_user.id, message.text)
    user_controller.add(User(message.from_user.id, message.text))
    await message.answer("Готово", reply_markup=main_keyboard(message.from_user.id))
    await state.clear()

