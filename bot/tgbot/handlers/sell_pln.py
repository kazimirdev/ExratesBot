from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext

from tgbot.states.buy_or_sell_state import BOS


async def sell_pln(cb: types.CallbackQuery, state: FSMContext):
    await cb.message.answer(text="Ile chcesz sprzedać PLN?")
    await BOS.choose_func_converter.set()
    await state.update_data(answer="sell")

def register_sell_pln(dp: Dispatcher):
    dp.register_callback_query_handler(
            sell_pln,
            text="sell_fiat",
            )
