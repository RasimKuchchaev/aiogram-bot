import asyncio
import datetime
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot
import re


# заблокировать
@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def read_mode_only(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    else:
        time = int(time)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    ReadOnlyPermissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False
    )
    try:
        await bot.restrict_chat_member(chat_id, user_id=member_id, permissions=ReadOnlyPermissions,
                                       until_date=until_date)
        await message.reply(f"Пользователь {member.get_mention(as_html=True)}"
                            f"запрещено писать на {time} минут. По причине: {comment}")
    except BadRequest:
        await message.answer("Пользователь является администратором")
    except Exception as err:
        await message.answer(f"{err.__class__.__name__}: {err}")


    service_message = await message.reply("Сообщение самоуничтожится через 5 секунд.")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


# разблокировать
@dp.message_handler(IsGroup(), Command("unro", prefixes="!/"), AdminFilter())
async def undo_read_mode_only(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False
    )
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Пользователь {member.full_name} был разблокирован")


# ban user
@dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)
    await message.reply(f"Пользователь {member.full_name} был забанен")


# ban user
@dp.message_handler(IsGroup(), Command("unban", prefixes="!/"), AdminFilter())
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.unban(user_id=member_id)
    await message.reply(f"Пользователь {member.full_name} был разбанен")