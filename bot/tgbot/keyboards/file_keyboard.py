from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


file_keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [InlineKeyboardButton(text="Menu głowne",
                callback_data="menu")],
            [InlineKeyboardButton(text="Kod żródłowy",
                url="https://github.com/Greenboyisyourdream/ExratesBot")]
            ])
