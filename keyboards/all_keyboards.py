from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from controllers.queue import queue
from create_bot import admins

def main_keyboard(user_telegram_id: int):
    keyboard_list = [
        [KeyboardButton(text="Показать очередь")],
        [KeyboardButton(text="Записаться в конец очереди")],
        [KeyboardButton(text="Предложить обмен")],
    ]
    if user_telegram_id in admins:
        keyboard_list.append([KeyboardButton(text="Админ панель")])

    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard

def choose_groupmate():
    keyboard_list = []
    for line in queue.show().split('\n'):
        keyboard_list.append([KeyboardButton(text=line)])

    keyboard = ReplyKeyboardMarkup(keyboard=keyboard_list, resize_keyboard=True, one_time_keyboard=True)
    return keyboard
