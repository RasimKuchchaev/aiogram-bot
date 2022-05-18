from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsForwarded(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        # Если сообщение переслано у него будет параметр forward_from_chat
        if message.forward_from_chat:
            # Проверяет перслано ли сообщение с канала (message.forward_from_chat.type == types.ChatType.CHANNEL)
            return message.forward_from_chat.type == types.ChatType.CHANNEL
