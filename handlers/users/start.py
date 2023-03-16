import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(
            fullname=message.from_user.full_name,
            username=message.from_user.username,
            telegram_id=message.from_user.id
        )
    except asyncpg.exceptions.UniqueViolationError:
        pass
        # user = await db.select_user(telegram_id=message.from_user.id)

    user = await db.select_user(telegram_id=message.from_user.id)

    count_users = await db.count_users()

    user_data = list(user)
    user_data_dict = dict(user)

    username = user.get('username')
    fullname = user[1]

    await message.answer(
         "\n".join(
             [
                 f"Привет, {message.from_user.full_name}!",
                 f"Ты был занесен в базу",
                 f"В базе <b>{count_users}</b> пользователей",
                 "",
                 f"<code>User: {username} - {fullname}",
                 f"{user_data=}",
                 f"{user_data_dict=}</code>"
             ]
         )
     )

    await message.answer(f"Привет, {message.from_user.full_name}!")
