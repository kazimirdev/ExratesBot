import json
import os

from dicttoxml2 import dicttoxml
from aiogram import Dispatcher, types

from tgbot.keyboards.file_keyboard import file_keyboard


async def get_crypto_file(cb: types.CallbackQuery):
    await cb.answer()
    answer = "Plik był wysłan"
    filename = f"Kryptowaluty {cb.message.date}."
    l_data = [l.split(" = ") for l in cb.message.text.split("\n")[1:]]
    d_data = {d[0]: d[1] for d in l_data}
    if cb.data == "cxml":
        filename += "xml"
        xml = dicttoxml(d_data).decode()
        with open(filename, "w") as f:
            f.write(str(xml))
    if cb.data == "cjson":
        filename += "json"
        with open(filename, "w") as f:
            json.dump(d_data, f)
    media = types.MediaGroup()
    media.attach_document(types.InputFile(filename))
    await cb.message.reply_media_group(media=media)
    await cb.message.answer(text=answer, reply_markup=file_keyboard)
    os.remove(filename)


def register_get_crypto_file(dp: Dispatcher):
    dp.register_callback_query_handler(get_crypto_file, text="cxml")
    dp.register_callback_query_handler(get_crypto_file, text="cjson")
