from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, Message, InputFile, MediaGroup

from loader import dp, bot


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=ContentType.VIDEO)
async def get_file_id_v(message: Message):
    await message.reply(message.video.file_id)

@dp.message_handler(Command("get_cat"))
async def send_cat(message: Message):
    photo_file_id = "AgACAgQAAxkBAAPkYoy3qv8UYbAOWUHqBFSLxIkPAlUAAl6rMRv5pOVTKoNAPOafcxUBAAMCAAN5AAMkBA"
    photo_url = "https://101kote.ru/upload/iblock/f3c/egeyskaya2.jpg"
    photo_bytes = InputFile(path_or_bytesio="photos/cat.jpg")
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_url,
                         caption="Вот тебе фото кота /more_cats")
    await message.answer_video("BAACAgIAAxkBAAPoYoy48RKWS7T1QY-cD3hNsCQoJaUAAuYYAAJE3GlIXapqLtrcipEkBA")

@dp.message_handler(Command("more_cats"))
async def send_cat(message: Message):
    album = MediaGroup()
    photo_file_id = "AgACAgQAAxkBAAPkYoy3qv8UYbAOWUHqBFSLxIkPAlUAAl6rMRv5pOVTKoNAPOafcxUBAAMCAAN5AAMkBA"
    photo_url = "https://101kote.ru/upload/iblock/f3c/egeyskaya2.jpg"
    photo_bytes = InputFile(path_or_bytesio="photos/cat.jpg")
    video_file_id = "BAACAgIAAxkBAAPoYoy48RKWS7T1QY-cD3hNsCQoJaUAAuYYAAJE3GlIXapqLtrcipEkBA"
    album.attach_photo(photo_file_id)
    album.attach_photo(photo_bytes)
    album.attach_photo(photo_url)
    album.attach_video(video_file_id,
                       caption="Вот видео где кот запрыгивает на кровать")

    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)




