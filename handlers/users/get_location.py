from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default import location_button
from loader import dp
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(Command("location"))
async def geo_location_button(message: types.Message):
    await message.answer(f"Отправьте нам свою локацию нажав на кнопку ниже!",
                         reply_markup=location_button.keyboard)

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    print(location)
    print(latitude, longitude)
    await message.answer(text=f"https://yandex.ru/maps/?text={latitude},{longitude}", reply_markup=ReplyKeyboardRemove(),
                         disable_web_page_preview=True)


