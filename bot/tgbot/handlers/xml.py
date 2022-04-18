import os
import dicttoxml

from aiogram import Dispatcher, types


async def get_crypto_xml(cb: types.CallbackQuery):
    file_name = f"Kryptowaluty {cb.message.date}.xml"
    data = [l.split(" = ") for l in cb.message.text.split("\n")[1:]]
    dict_data = {d[0]: d[1] for d in data}
    xml = dicttoxml.dicttoxml(dict_data)
    with open(f"{file_name}", "w") as f:
        f.write(str(xml)[2:-1])
        """
        In brackets is a crutch so that the file can be read normally, 
        then someday I will do it normally
        """
    media = types.MediaGroup()
    media.attach_document(types.InputFile(file_name))
    await cb.message.reply_media_group(media=media)
    os.remove(file_name)


def register_get_crypro_xml(dp: Dispatcher):
    dp.register_callback_query_handler(get_crypto_xml, text="xml")
