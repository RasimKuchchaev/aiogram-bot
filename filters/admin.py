from aiogram import types

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), user_id =[650242009], text = "admin")
@dp.message_handler(IsPrivate(), user_id =[123456789, 650242009], text = "secret")
async def admin_chat_secret(message: types.Message):
    await message.answer("Это секретное сообщение вызваное одним из администраторов в личной переписке")

