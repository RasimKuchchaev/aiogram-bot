from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Contact", request_contact=True)
        ]
    ],
    resize_keyboard=True
)