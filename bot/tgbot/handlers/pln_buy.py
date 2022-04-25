from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext

from tgbot.states.buy_or_sell_state import BOS


async def buy_pln(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    answer = "Ile chcesz sprzedać waluty żeby otrzymać PLN?"
    await cb.message.answer(text=answer)
    await BOS.choose_func_converter.set()
    await state.update_data(answer="buy")

def register_buy_pln(dp: Dispatcher):
    dp.register_callback_query_handler(
            buy_pln,
            text="buy_fiat"
            )
