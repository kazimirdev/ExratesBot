import json
import os

from dicttoxml2 import dicttoxml
from aiogram import Dispatcher, types

from tgbot.keyboards.file_keyboard import file_keyboard


async def get_fiat_file(cb: types.CallbackQuery):
    await cb.answer()
    answer = "Plik był wysłan"
    filename = f"Fiducjarne waluty {cb.message.date}."
    l_data = cb.message.text.split("\n")[1:]
    d_data = {l_data[i]: 
        {l_data[i+1].split(": ")[0]: l_data[i+1].split(": ")[1]} |
        {l_data[i+2].split(": ")[0]: l_data[i+2].split(": ")[1]} |
        {l_data[i+3].split(": ")[0]: l_data[i+3].split(": ")[1]}
         for i in range(0, len(l_data), 4)}
    if cb.data == "fxml":
        filename += "xml"
        xml = dicttoxml(d_data).decode()
        with open(filename, "w") as f:
            f.write(str(xml))
    if cb.data == "fjson":
        filename += "json"
        with open(filename, "w") as f:
            json.dump(d_data, f)
    media = types.MediaGroup()
    media.attach_document(types.InputFile(filename))
    await cb.message.reply_media_group(media=media)
    await cb.message.answer(text=answer, reply_markup=file_keyboard)
    os.remove(filename)


def register_get_fiat_file(dp: Dispatcher):
    dp.register_callback_query_handler(get_fiat_file, text="fxml")
    dp.register_callback_query_handler(get_fiat_file, text="fjson")

