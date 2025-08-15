from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config

admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]
assistants = [int(assistant_id) for assistant_id in config('ASSISTANTS').split(',')]

bot = Bot(token=config('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dispatcher = Dispatcher(storage=MemoryStorage())