from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bs_keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Pobierz .json",
                callback_data="bsjson"),
            InlineKeyboardButton(
                text="Pobierz .xml",
                callback_data="bsxml")],
            [InlineKeyboardButton(
                text="Menu główne",
                callback_data="menu")]
            ])
