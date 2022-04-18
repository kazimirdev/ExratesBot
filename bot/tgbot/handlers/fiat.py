import asyncio
from aiogram import Dispatcher, types

from tgbot.keyboards.data_keyboard import data_keyboard
from tgbot.misc.fiatparse import fiat_parser


async def get_fiat(cb: types.CallbackQuery):
    fiats = await fiat_parser()
    answer = 'Fiducjarne kursy walut:\n'
    for fiat in fiats:
        lines = [
                f"{fiat[0]}",
                f"Różnica za dobę: {fiat[1]}",
                f"Kupno: {fiat[2]}",
                f"Sprzedaż: {fiat[3]}\n"
                ]
        answer += "\n".join(lines)
    await cb.message.reply(answer, reply_markup=data_keyboard)


def register_get_fiat(dp: Dispatcher):
    dp.register_callback_query_handler(get_fiat, text="fiat_data")
