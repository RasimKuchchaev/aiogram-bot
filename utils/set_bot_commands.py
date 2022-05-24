from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("get_cat", "Прислать кота"),
            types.BotCommand("more_cats", "Пристаь больше котов"),
        ]
    )
