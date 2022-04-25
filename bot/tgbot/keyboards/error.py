from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

error_keyboard = InlineKeyboardMarkup(row_width=1,
        inline_keyboard=[[
            InlineKeyboardButton(
                text="Menu główne",
                callback_data="menu"
            )]])
