from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from controllers.queue import queue
from keyboards.all_keyboards import main_keyboard, choose_groupmate


class OrderSwap(StatesGroup):
    choosing_groupmate = State()

queue_router = Router()

@queue_router.message(F.text == "Показать очередь")
async def show(message: Message):
    await message.answer(queue.show(), reply_markup=main_keyboard(message.from_user.id))

@queue_router.message(F.text == "Записаться в конец очереди")
async def append(message: Message):
    queue.append(message.from_user.id)
    await message.answer(queue.show(), reply_markup=main_keyboard(message.from_user.id))

@queue_router.message(StateFilter(None), F.text == "Предложить обмен")
async def swap_choosing(message: Message, state: FSMContext):
    await message.answer("Выбери с кем хочешь поменяться:", reply_markup=choose_groupmate())
    await state.set_state(OrderSwap.choosing_groupmate)

@queue_router.message(OrderSwap.choosing_groupmate)
async def swap(message: Message, state: FSMContext):
    error = do_some_logic(message.text)
    if error:
        await message.answer("Ошибка", reply_markup=main_keyboard(message.from_user.id))
    else:
        await message.answer("Готово", reply_markup=main_keyboard(message.from_user.id))
    await state.clear()
