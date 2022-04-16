from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_keyboard = InlineKeyboardMarkup(row_width=5,
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Fiducjarne Waluty",
                callback_data="fiat_data"),
            InlineKeyboardButton(
                text="Kryptowalyty",
                callback_data="crypto_data")],
            [InlineKeyboardButton(
                text="Kupic PLN", 
                callback_data="buy_fiat"),
            InlineKeyboardButton(
                text="Sprzedać PLN",
                callback_data="sell_fiat")],
            [InlineKeyboardButton(
                text="Pomnożyć Kryptowalyty",
                callback_data="mult_crypto"),
            InlineKeyboardButton(
                text="Pomnożyć Fiducjarne walyty",
                callback_data="mult_fiat")],
            [InlineKeyboardButton(
                text="Więcej o kryprocie",
                callback="more_crypro")],
            [InlineKeyboardButton(
                text="Kod źródłowy",
                url="https://github.com/Greenboyisyourdream/ExratesBot")]
            ]
        )
