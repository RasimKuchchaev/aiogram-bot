from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import contact_button
from loader import dp
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(Command("contact"))
async def geo_location_button(message: types.Message):
    await message.answer(f"Отправьте нам свой номер телефона нажав на кнопку ниже!",
                         reply_markup=contact_button.keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_location(message: types.Message):
    contact = message.contact
    await message.answer(text=f"Спасибо, {contact.full_name}\n"
                              f"Ваш номер {contact.phone_number}", reply_markup=ReplyKeyboardRemove())