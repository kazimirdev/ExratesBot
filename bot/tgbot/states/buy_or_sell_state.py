from aiogram.dispatcher.filters.state import State, StatesGroup


class BOS(StatesGroup):
    choose_func_converter = State()
