from aiogram import Dispatcher, types
from aiogram.dispatcher.storage import FSMContext

from tgbot.keyboards import menu_keyboard
from tgbot.states.buy_or_sell_state import BOS


async def menu(instance: types.Message | types.CallbackQuery,
        state: FSMContext):
    state.reset_state(with_data=True)
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
        await state.reset_state(with_data=True)
    if isinstance(instance, types.CallbackQuery):
        await instance.answer()
        await instance.message.answer(
                '\n'.join(
                    answer[-2:]
                    ),
                reply_markup=menu_keyboard
                )
        await state.reset_state(with_data=True)

def register_menu(dp: Dispatcher):
    dp.register_message_handler(
            menu,
            commands=['start'],
            state="*")
    dp.register_callback_query_handler(
            menu,
            text='menu',
            state="*")
