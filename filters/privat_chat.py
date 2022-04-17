from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    async def check(self, message: types.Message) -> bool:
# Проверка на приватность чата
        # if message.chat.type == "privete":
        #     return True
        # else:
        #     return False
# или
        return message.chat.type == types.ChatType.PRIVATE