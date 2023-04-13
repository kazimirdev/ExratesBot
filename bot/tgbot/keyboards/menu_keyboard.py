from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_keyboard = InlineKeyboardMarkup(
        row_width=4,
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Kursy walut",
                callback_data="fiat_data")],
            [InlineKeyboardButton(
                text="Kupic PLN", 
                callback_data="buy_fiat"),
            InlineKeyboardButton(
                text="Sprzedać PLN",
                callback_data="sell_fiat")],
            [InlineKeyboardButton(
                text="Kod źródłowy",
                url="https://github.com/Greenboyisyourdream/ExratesBot")]
            ]
        )
