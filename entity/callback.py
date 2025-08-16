from aiogram.filters.callback_data import CallbackData


class AgreementCallback(CallbackData, prefix="agreement"):
    name: str
    agree: bool
    source_id: int