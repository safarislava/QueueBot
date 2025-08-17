from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from controllers.queue_manager import queue_manager
from controllers.user import user_controller
from create_bot import bot
from entity.callback import AgreementCallback
from entity.state import VerificationAppend, OrderSwap
from keyboards.all_keyboards import main_keyboard, choose_groupmate_keyboard, agreement_keyboard

queue_router = Router()

@queue_router.message(F.text == "Показать очередь")
async def show(message: Message) -> None:
    await message.answer(queue_manager.get_queue().show(), reply_markup=main_keyboard(message.from_user.id))

@queue_router.message(StateFilter(None), F.text == "Записаться в конец очереди")
async def append(message: Message, state: FSMContext) -> None:
    if queue_manager.get_queue().exist(message.from_user.id):
        await message.answer("Напишите: ПОДТВЕРЖДАЮ", reply_markup=None)
        await state.set_state(VerificationAppend.verification)
    else:
        queue_manager.get_queue().append(message.from_user.id)
        await message.answer(queue_manager.get_queue().show(), reply_markup=main_keyboard(message.from_user.id))

@queue_router.message(VerificationAppend.verification)
async def append_verify(message: Message, state: FSMContext) -> None:
    if message.text == "ПОДТВЕРЖДАЮ":
        queue_manager.get_queue().append(message.from_user.id)
    else:
        await message.answer("Не подтверждено")
    await message.answer(queue_manager.get_queue().show(), reply_markup=main_keyboard(message.from_user.id))
    await state.clear()

@queue_router.message(StateFilter(None), F.text == "Предложить обмен")
async def swap_choosing(message: Message, state: FSMContext) -> None:
    if len(queue_manager.get_queue().value) == 0:
        await message.answer("Очередь пуста", reply_markup=main_keyboard(message.from_user.id))
        return

    await message.answer("Выбери с кем хочешь поменяться:", reply_markup=choose_groupmate_keyboard())
    await state.set_state(OrderSwap.choosing_groupmate)

@queue_router.message(OrderSwap.choosing_groupmate)
async def swap(message: Message, state: FSMContext) -> None:
    # error = False
    # if not message.text in queue.show().split("\n"):
    #     error = True
    name = message.text.split(" ", maxsplit=1)[1]
    user = user_controller.get_user_by_str(name)

    await bot.send_message(chat_id=user.id,
                     text=f"Принять обмен с {user_controller.get_user_by_int(message.from_user.id).name}",
                     reply_markup=agreement_keyboard(message.from_user.id))
    await message.answer("Запрос отправлен", reply_markup=main_keyboard(message.from_user.id))
    await state.clear()

@queue_router.callback_query(AgreementCallback.filter(F.name == "swap"))
async def agreement_callback(query: CallbackQuery, callback_data: AgreementCallback) -> None:
    name = user_controller.users.get(query.from_user.id).name
    if callback_data.agree:
        queue_manager.get_queue().swap(callback_data.source_id, query.from_user.id)
        await bot.send_message(chat_id=callback_data.source_id, text=f"Обмен с {name} произошёл успешно")
    else:
        await bot.send_message(chat_id=callback_data.source_id, text=f"Обмен с {name} отклонён")

    await query.message.delete()
    await query.answer(text="Готово")
