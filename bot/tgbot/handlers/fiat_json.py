import os
import json

from aiogram import Dispatcher, types

from tgbot.keyboards.file_keyboard import file_keyboard


async def get_fiat_json(cb: types.CallbackQuery):
    answer = "Plik był wysłan"
    file_name = f"Fiducjarne waluty {cb.message.date}.json"
    md = cb.message.text.split("\n")[1:]
    data = {md[i]:
        {md[i+1].split(": ")[0]: md[i+1].split(": ")[1]} |
        {md[i+2].split(": ")[0]: md[i+2].split(": ")[1]} |
        {md[i+3].split(": ")[0]: md[i+3].split(": ")[1]}
         for i in range(0, len(md), 4)}
    with open(file_name, "w") as fn:
        json.dump(data, fn)
    media = types.MediaGroup()
    media.attach_document(types.InputFile(file_name))
    await cb.message.reply_media_group(media=media)
    await cb.message.answer(text=answer, reply_markup=file_keyboard)
    os.remove(file_name)


def register_get_fiat_json(dp: Dispatcher):
    dp.register_callback_query_handler(get_fiat_json, text="fjson")
