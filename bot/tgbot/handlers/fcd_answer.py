import logging
from aiogram import types, Dispatcher
from aiogram.dispatcher.handler import SkipHandler
from aiogram.dispatcher.storage import FSMContext

from tgbot.misc.specific_cryptoparse import specific_crypro_parser
from tgbot.keyboards.error import error_keyboard
from tgbot.keyboards.fcd_keyboard import fcd_keyboard
from tgbot.states.buy_or_sell_state import BOS

async def get_answer_fcd(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    logging.info(f'Got into handler = get_answer_fcd. State data: {state_data}')
    if state_data.get("answer") == "crypto_data":
        data = await specific_crypro_parser(message.text)
        if data is None:
            await message.answer(
                    text="Nie wiem tej kryptowaluty",
                    reply_markup=error_keyboard)
        else:
            answer = [f"{d[0]}: {d[1]}" for d in data]
            await message.answer(
                    text="\n".join(answer),
                    reply_markup=fcd_keyboard)
            await state.reset_state(with_data=True)
    else:
        raise SkipHandler()

def register_get_answer_fcd(dp: Dispatcher):
    dp.register_message_handler(
            get_answer_fcd,
            state=BOS.choose_func_converter)
