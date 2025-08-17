from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from entity.callback import AgreementCallback
from controllers.queue_manager import queue_manager
from create_bot import admins

def main_keyboard(user_id: int) -> ReplyKeyboardMarkup:
    keyboard_list = [
        [KeyboardButton(text="Показать очередь")],
        [KeyboardButton(text="Записаться в конец очереди")],
        [KeyboardButton(text="Предложить обмен")],
    ]
    if user_id in admins:
        keyboard_list.append([KeyboardButton(text="Админ панель")])

    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_list, resize_keyboard=True)
    return keyboard

def choose_groupmate_keyboard() -> ReplyKeyboardMarkup:
    keyboard_list = []
    for line in queue_manager.get_queue().show().split('\n'):
        keyboard_list.append([KeyboardButton(text=line)])

    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

def agreement_keyboard(user_id: int) -> InlineKeyboardMarkup:
    agree_callback = AgreementCallback(name="swap", agree=True, source_id=user_id).pack()
    disagree_callback = AgreementCallback(name="swap", agree=False, source_id=user_id).pack()

    keyboard_list = [[InlineKeyboardButton(text="Согласен", callback_data=agree_callback),
                      InlineKeyboardButton(text="Нет", callback_data=disagree_callback)]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
    return keyboard

def admin_keyboard() -> ReplyKeyboardMarkup:
    keyboard_list = [[KeyboardButton(text="Сохранить"), KeyboardButton(text="Загрузить")],
                     [KeyboardButton(text="Показать очереди")],
                     [KeyboardButton(text="Задать предмет")]]
    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard
