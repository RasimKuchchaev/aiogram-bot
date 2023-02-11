from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import MediaGroup, InputFile

from loader import dp


@dp.message_handler(Command('medio_group'))
async def catch_medio_group(message: types.Message):
    albom = MediaGroup()
    albom.attach_photo('https://i.pinimg.com/736x/2d/be/24/2dbe243ad51509a80c6627868807b1ea.jpg')
    albom.attach_photo('AgACAgIAAxkBAAIER2Pn52Wa76eSx0vVoJLlub2LsF7wAALlwDEbIJpAS4cgKeFNGPRkAQADAgADeQADLgQ')
    albom.attach_photo(types.InputFile(path_or_bytesio=r"C:\Users\admin\Downloads\5286e36dbc7a8.jpg"))
    await message.answer_media_group(media=albom)

@dp.message_handler()
async def catch_text(message: types.Message):
    await message.answer("Вы прислали текст")\


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def catch_doc(message: types.Message):
    await message.document.download()
    await message.reply("Документ скачан\n"
                        f"<pre>FILR ID = {message.document.file_id}</pre>",
                        parse_mode="HTML")


# @dp.message_handler(content_types=types.ContentTypes.AUDIO | types.ContentTypes.VIDEO)
@dp.message_handler(content_types=types.ContentType.AUDIO)
async def catch_audio(message: types.Message):
    await message.audio.download()
    await message.reply(
        "Аудиозапись скачана\n"
        f"<pre>FILR ID = {message.audio.file_id}</pre>",
        parse_mode="HTML")


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def catch_video(message: types.Message):
    # await message.video.download()
    await message.video.download(destination_dir=r"D:\test")
    await message.reply(
        "Видеозапись скачана\n"
        f"<pre>FILR ID = {message.video.file_id}</pre>",
        parse_mode="HTML")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def catch_photo(message: types.Message):
    # await message.photo[-1].download(destination_file=r"D:\test\11.jpg")
    await message.photo[-1].download(destination_dir=r"D:\test")
    await message.reply(
        "Фотография скачана\n"
        f"<pre>FILR ID = {message.photo[-1].file_id}</pre>",
        parse_mode="HTML")

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def catch_photo(message: types.Message):
    # await message.photo[-1].download(destination_file=r"D:\test\11.jpg")
    await message.photo[-1].download(destination_dir=r"D:\test")
    await message.reply(
        "Фотография скачана\n"
        f"<pre>FILR ID = {message.photo[-1].file_id}</pre>",
        parse_mode="HTML")


@dp.message_handler(content_types=types.ContentType.ANY)
async def catch_any(message: types.Message):
    await message.reply(f"Вы прислали ... {message.content_type}",
        parse_mode="HTML")




