from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Location", request_location=True)
        ]
    ],
    resize_keyboard=True
)