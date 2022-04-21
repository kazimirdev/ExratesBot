import os
import dicttoxml2

from aiogram import Dispatcher, types

from tgbot.keyboards.file_keyboard import file_keyboard

async def get_crypto_xml(cb: types.CallbackQuery):
    answer = "Plik był wysłan"
    file_name = f"Kryptowaluty {cb.message.date}.xml"
    data = [l.split(" = ") for l in cb.message.text.split("\n")[1:]]
    dict_data = {d[0]: d[1] for d in data}
    xml = dicttoxml2.dicttoxml(dict_data).decode()
    with open(file_name, "w") as f:
        f.write(str(xml))
    media = types.MediaGroup()
    media.attach_document(types.InputFile(file_name))
    await cb.message.reply_media_group(media=media)
    await cb.message.answer(text=answer, reply_markup=file_keyboard)
    os.remove(file_name)


def register_get_crypto_xml(dp: Dispatcher):
    dp.register_callback_query_handler(get_crypto_xml, text="cxml")
