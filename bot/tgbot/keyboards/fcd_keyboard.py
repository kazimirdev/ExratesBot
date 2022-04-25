from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


fcd_keyboard = InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Pobierz .json",
                callback_data="fcdjson"
                ),
            InlineKeyboardButton(
                text="Pobierz .xml",
                callback_data="fcdxml")
                ],
            [InlineKeyboardButton(
                text="Menu główne",
                callback_data="menu"
                )],
            ])
