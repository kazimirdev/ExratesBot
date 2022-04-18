from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


data_keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Pobierz .json",
                callback_data='json'
                ),
            InlineKeyboardButton(
                text='Pobierz .xml',
                callback_data='xml'
                )],
            [InlineKeyboardButton(text='Menu głowne', callback_data='menu')]
            ]
        )
