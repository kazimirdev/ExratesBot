import logging

from decimal import Decimal, InvalidOperation

from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext

from tgbot.misc.fiatparse import fiat_parser
from tgbot.keyboards.buy_sell_keyboard import bs_keyboard
from tgbot.keyboards.error import error_keyboard 
from tgbot.states.buy_or_sell_state import BOS

async def answer_pln(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    
    logging.info(f'{message.text=}')
    try:
        answer = ""
        fiat = await fiat_parser()
        l_answer = []
        
        if state_data.get("answer") == "buy":
            answer += "Kupno\n"
            for f in fiat:
                l_answer += [
                        f"{f[0]}: {Decimal(f[2])*Decimal(message.text)}"]
        answer += "\n".join(l_answer)
        
        if state_data.get("answer") == "sell":
            answer += "Sprzedaż\n"
            for f in fiat:
                l_answer += [
                        f"{f[0]}: {round(float(Decimal(message.text)/Decimal(f[3])) ,4)}"]
            answer += "\n".join(l_answer)

        await message.reply(text=answer,
                reply_markup=bs_keyboard)
        await state.reset_state(with_data=True)
    
    except InvalidOperation:
        await message.reply(text="To nie jest liczbą",
                reply_markup=error_keyboard)



def register_answer_pln(dp: Dispatcher):
        dp.register_message_handler(
                answer_pln,
                state=BOS.choose_func_converter
                )
