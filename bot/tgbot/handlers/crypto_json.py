import json
import os

from aiogram import Dispatcher, types

from tgbot.keyboards.file_keyboard import file_keyboard


async def get_crypto_json(cb: types.CallbackQuery):
    answer = "Plik był wysłan"
    file_name = f"Kryprowalyty {cb.message.date}.json"
    data = [l.split(" = ") for l in cb.message.text.split("\n")[1:]]
    file = {d[0]: d[1] for d in data}
    with open(file_name, "w") as fn:
        json.dump(file, fn)
    media = types.MediaGroup()
    media.attach_document(types.InputFile(file_name))
    await cb.message.reply_media_group(media=media)
    await cb.message.answer(text=answer, reply_markup=file_keyboard)
    os.remove(file_name)


def register_get_crypto_json(dp: Dispatcher):
    dp.register_callback_query_handler(get_crypto_json, text="cjson")
