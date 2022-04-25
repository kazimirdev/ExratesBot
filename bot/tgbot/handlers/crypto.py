from aiogram import Dispatcher, types
from decimal import Decimal

from tgbot.keyboards.crypto_data_keyboard import data_keyboard
from tgbot.misc.cryptoparse import crypto_parser


async def get_crypto(cb: types.CallbackQuery):
    await cb.answer()
    result = await crypto_parser()
    answer = "Kursy kryptowalut:\n"
    for r in result.items():
        answer += f"{r[0]}-USD = {Decimal(r[1][1:].replace(',', ''))}\n"
    await cb.message.reply(answer, reply_markup=data_keyboard)


def register_get_crypto(dp: Dispatcher):
    dp.register_callback_query_handler(get_crypto, text="crypto_data")
