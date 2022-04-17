import asyncio
from aiogram import Dispatcher, types

from tgbot.misc.fiatparse import fiat_parser


async def get_fiat(cb: types.CallbackQuery):
    fiat_parse = await fiat_parser()
    fiat_loop = asyncio.get_event_loop()
    fiats = fiat_loop.run_until_complete(fiat_parse())
    answer = 'Fiducjarne kursy walut:\n'
    for fiat in fiats:
        lines = [
                f"{fiat[0]}",
                f"Różnica za dobę: {fiat[1]}",
                f"Kupno: {fiat[2]}",
                f"Sprzedaż: {fiat[3]}\n"
                ]
        answer += "\n".join(lines)
    await cb.message.reply(answer)


def register_get_fiat(dp: Dispatcher):
    dp.register_callback_query_handler(get_fiat, text="fiat_data")
