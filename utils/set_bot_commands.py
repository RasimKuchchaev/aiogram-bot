from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("set_photo", "Устанавить фото в чате"),
            types.BotCommand("set_title", "Установить название группы"),
            types.BotCommand("set_description", "Установить описание группы"),
            types.BotCommand("ro", "Режим Read Only"),
            types.BotCommand("unro", "Отключить RO"),
            types.BotCommand("ban", "Забанить"),
            types.BotCommand("unban", "Разбанить"),
        ]
    )
