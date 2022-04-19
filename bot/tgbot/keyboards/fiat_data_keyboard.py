from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


data_keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Pobierz .json",
                callback_data='fjson'
                ),
            InlineKeyboardButton(
                text='Pobierz .xml',
                callback_data='fxml'
                )],
            [InlineKeyboardButton(text='Menu głowne', callback_data='menu')]
            ]
        )
