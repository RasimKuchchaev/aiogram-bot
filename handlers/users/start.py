import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    non_existing_user = 666666

# Не попадает в эррор хендлер, обрабатывается тут с помощью try
    try:
        await message.answer("Неправильно закрыт <b>тег<b>")
    except Exception as err:
        await message.answer(f"Не попало в эррор хендлер. Ошибка: {err}")

    # Не попадает в эррор хендлер
    try:
        await bot.send_message(chat_id=non_existing_user, text="Не существует пользователь")
    except Exception as err:
        await message.answer(f"Не попало в эррор хендлер. Ошибка: {err}")

    # Попадает отсюда в эррор хендлер
    await message.answer("Не существует <kek>тега</kek>")
    logging.info("Это не выполнится, но бот не упадет.")

    # Все что ниже - не выполнится, но бот не упадет

    await message.answer("...")

