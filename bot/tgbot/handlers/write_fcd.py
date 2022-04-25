from aiogram import Dispatcher, types


# fcd - full crypto's data
async def write_name_fcd(cb: types.CallbackQuery):
    answer = [
            "Napisz nazwę nazwę kryptowaluty:",
            "",
            "(Pisz pęlny tytuł kryptowaluty."
            "Ja nie zrozumiem ciebie, jeśli napiszesz",
            "krótky tytuł waluty, narptykład: "
            'nie "btc", a "bitcoin".)'
            ]
    await cb.message.answer(text="\n".join(answer))


def register_write_name_fcd(dp: Dispatcher):
    dp.register_callback_query_handler(write_name_fcd)
