from aiogram import Dispatcher, types

from tgbot.keyboards import menu_keyboard


async def menu(instance: types.Message | types.CallbackQuery):
    answer = [
            'Cześć, {}!',
            'Ten bot daje ciebie moźliwość',
            'uzyskać kursy krypro-',
            'i fiducjarnych walut.',
            '',
            'Wybierz w menu to',
            'co potrzebujesz:'
            ]
    if isinstance(instance, types.Message):
        await instance.answer(
                '\n'.join(
                    a.format(instance.from_user.full_name) for a in answer
                    ),
                reply_markup=menu_keyboard
                )
    if isinstance(instance, types.CallbackQuery):
        await instance.message.answer(
                '\n'.join(
                    answer[-2:]
                    ),
                reply_markup=menu_keyboard
                )

def register_menu(dp: Dispatcher):
    dp.register_message_handler(menu, commands=['start'])
    dp.register_callback_query_handler(menu, text='menu')
