import json
import os

from dicttoxml2 import dicttoxml
from aiogram import types, Dispatcher

from tgbot.keyboards.file_keyboard import file_keyboard


async def get_fcd_file(cb: types.CallbackQuery):
    await cb.answer()
    answer = "Plik był wysłan"
    # cc - cryptocurrency
    cc_name = cb.message.text.split("\n")[0].split(":")[0]
    cc_name.replace("Cena ", "")
    filename = f"Wszystko o {cc_name} {cb.message.date}."
    # d - dictionary, l - list
    l_data = [l.split(": ") for l in cb.message.text.split("\n")]
    d_data = {d[0]: d[1] for d in l_data}
    if cb.data == "fcdxml":
        filename += "xml"
        xml_data = dicttoxml(d_data).decode()
        with open(filename, "w") as f:
            f.write(xml_data)
    if cb.data == "fcdjson":
        filename += "json"
        with open(filename, "w") as f:
            json.dump(d_data, f)
    media = types.MediaGroup()
    media.attach_document(types.InputFile(filename))
    await cb.message.reply_media_group(media=media)
    await cb.message.answer(text=answer, reply_markup=file_keyboard)
    os.remove(filename)


def register_get_fcd(dp: Dispatcher):
    dp.register_callback_query_handler(
            get_fcd_file,
            text="fcdxml")
    dp.register_callback_query_handler(
            get_fcd_file,
            text="fcdjson")
