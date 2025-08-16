from aiogram.fsm.state import StatesGroup, State


class OrderSwap(StatesGroup):
    choosing_groupmate = State()

class VerificationAppend(StatesGroup):
    verification = State()

class Registration(StatesGroup):
    registration = State()