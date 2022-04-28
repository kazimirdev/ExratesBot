import json
import os

from aiogram import types, Dispatcher
from dicttoxml2 import dicttoxml

from tgbot.keyboards.file_keyboard import file_keyboard


async def get_pln_file(cb: types.CallbackQuery):
    await cb.answer()
    answer = "Plik był wysłan"
    part_of_filename = cb.message.text.split('\n')[0]
    filename = f"{part_of_filename} PLN {cb.message.date}."
    l_data = [i.split(": ") for i in cb.message.text.split("\n")[1:]]
    d_data = {d[0]: d[1] for d in l_data}
    if cb.data == 'bsxml':
        filename += "xml"
        xml = dicttoxml(d_data).decode()
        with open(filename, "w") as f:
            f.write(xml)
    if cb.data == "bsjson":
        filename += "json"
        with open(filename, "w") as f:
            json.dump(d_data, f)
    media = types.MediaGroup()
    media.attach_document(types.InputFile(filename))
    await cb.message.reply_media_group(media=media)
    await cb.message.answer(text=answer, reply_markup=file_keyboard)
    os.remove(filename)


def register_get_pln_file(dp: Dispatcher):
    dp.register_callback_query_handler(get_pln_file, text="bsxml")
    dp.register_callback_query_handler(get_pln_file, text="bsjson")
