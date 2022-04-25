from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_keyboard = InlineKeyboardMarkup(
        row_width=4,
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
                text="Więcej o kryprowalucie",
                callback_data="more_crypto")],
            [InlineKeyboardButton(
                text="Kod źródłowy",
                url="https://github.com/Greenboyisyourdream/ExratesBot")]
            ]
        )
