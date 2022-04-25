from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext

from tgbot.states.buy_or_sell_state import BOS

# fcd - full crypto's data
async def write_name_fcd(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    answer = [
            "Napisz nazwę nazwę kryptowaluty:",
            "",
            "(Pisz pęlny tytuł kryptowaluty."
            "Ja nie zrozumiem ciebie jeśli ty",
            "napiszesz krótky tytuł waluty, narptykład: "
            'nie "btc", a "bitcoin".)'
            ]
    await cb.message.answer(text="\n".join(answer))
    await BOS.choose_func_converter.set()
    await state.update_data(answer="crypto_data")


def register_write_name_fcd(dp: Dispatcher):
    dp.register_callback_query_handler(
            write_name_fcd,
            text="more_crypto")
