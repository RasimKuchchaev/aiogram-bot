import re
from aiogram.dispatcher.filters import CommandStart
from aiogram import types
from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from loader import dp

@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")), IsPrivate())
async def bor_start_m(message: types.Message):
    diplink = message.get_args()
    await message.answer(f"Ты нажал на старт и передал diplinlk: {diplink} \n"
                         f"Привет, {message.from_user.full_name}!")


@dp.message_handler(CommandStart(),IsPrivate())
async def bor_start_m(message: types.Message):
    diplink_greate_link = await get_start_link(payload="123")
    await message.answer(f"Ты нажал на старт и у Вас нет Diplinka\n"
                         f" Новый Diplink создан: {diplink_greate_link}")