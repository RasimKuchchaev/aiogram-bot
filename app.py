import logging
from aiogram import executor
from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    logging.info("Создаем подключение к базе данных")
    await db.create()

    await db.create_table_user()

    # await db.drop_user()

    logging.info("Создаем таблицу пользователей")
    await db.create_table_user()
    logging.info("Готово")

    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

