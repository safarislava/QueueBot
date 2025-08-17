from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import create_bot
from controllers.queue_manager import queue_manager
from entity.state import SetQueue
from keyboards.all_keyboards import admin_keyboard, main_keyboard

admin_router = Router()

@admin_router.message(F.text == "Админ панель")
async def admin(message: Message) -> None:
    if not message.from_user.id in create_bot.admins:
        return
    await message.answer(str(message.from_user.id), reply_markup=admin_keyboard())

@admin_router.message(F.text == "Cохранить")
async def save(message: Message) -> None:
    if not message.from_user.id in create_bot.admins:
        return
    queue_manager.save()
    await message.answer("Готово", reply_markup=main_keyboard(message.from_user.id))

@admin_router.message(F.text == "Загрузить")
async def load(message: Message) -> None:
    if not message.from_user.id in create_bot.admins:
        return
    queue_manager.load()
    await message.answer("Готово", reply_markup=main_keyboard(message.from_user.id))

@admin_router.message(F.text == "Показать очереди")
async def show(message: Message) -> None:
    if not message.from_user.id in create_bot.admins:
        return
    await message.answer(str(queue_manager.queues.keys()), reply_markup=main_keyboard(message.from_user.id))

@admin_router.message(StateFilter(None), F.text == "Задать предмет")
async def ask_queue(message: Message, state: FSMContext) -> None:
    if not message.from_user.id in create_bot.admins:
        return
    await message.answer("Введи название предмета", reply_markup=main_keyboard(message.from_user.id))
    await state.set_state(SetQueue.setting)

@admin_router.message(SetQueue.setting)
async def set_queue(message: Message, state: FSMContext) -> None:
    if not message.from_user.id in create_bot.admins:
        return
    queue_manager.set_name(message.text)
    await state.clear()