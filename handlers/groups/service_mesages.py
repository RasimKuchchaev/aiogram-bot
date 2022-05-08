from filters import IsGroup
from loader import dp, bot
from aiogram import types


# Новый пользователь в чате
@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Привет, {members}.")

# Пользователь удален из чата
@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    # пользователь вышел из чата
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} вышел из чата")
    # пользователь удален ботом
    elif message.left_chat_member.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} был удален из чата "
                             f"пользователем {message.from_user.get_mention(as_html=True)}.")