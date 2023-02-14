from aiogram import types
from io import BytesIO
from loader import dp
from pathlib import Path        # библиотека для путей


# @dp.message_handler(content_types=types.ContentType.AUDIO)
# async def get_audio(message: types.Message):
#     file_id = message.audio.file_id
#     await message.answer(text=file_id)
#     # await message.answer_document(document='CQACAgIAAxkBAAIEeWPqaxKUhYgpxRvsfwI4YNOoCW4oAAI8KQACRFRQS9zvt8jdF4DpLgQ')
#     await message.answer_document(document=file_id)
#     await dp.bot.send_document(chat_id=message.chat.id, document='CQACAgIAAxkBAAIEeWPqaxKUhYgpxRvsfwI4YNOoCW4oAAI8KQACRFRQS9zvt8jdF4DpLgQ')


# сохранение документа в каталог
@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def download_document(message: types.Message):
    path_to_download = Path().joinpath("items", "categories", "subcategories", "photo")     # items\categories\subcategories\photo
    path_to_download.mkdir(parents=True, exist_ok=True)
    # Если parents=True, то будут созданы все отсутствующие каталоги нового пути
    # Если exist_ok=True, то исключения FileExistsError(каталог уже существует) будут игнорироваться
    path_to_download = path_to_download.joinpath(message.document.file_name)

    await message.document.download(destination_file=path_to_download)
    await message.answer(f"Документ был сохранен в путь: {path_to_download}")
    await dp.bot.send_document(chat_id=message.chat.id, document=message.document.file_id)


@dp.message_handler(content_types=types.ContentType.ANY)
async def get_any(message: types.Message):
    if message.document:
        await message.answer(text="document")
        file_id = message.document.file_id
    elif message.audio:
        await message.answer(text="audio")
        file_id = message.audio.file_id
    await message.answer_document(document=file_id)


# # конвертация фото в документ
# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def convert_photo_to_document(message: types.Message):
#     await message.answer(text="convert_photo")
#     save_to_io = BytesIO()
#     # await message.photo[-1].download(destination=save_to_io)      # destination - deprecated
#     await message.photo[-1].download(destination_file=save_to_io)
#     await message.answer_document(document=types.InputFile(save_to_io, filename="photo.jpg"))
#
# # конвертация документа в фото
# @dp.message_handler(content_types=types.ContentType.DOCUMENT)
# async def convert_document_to_photo(message: types.Message):
#     await message.answer(text="convert_document_to_photo")
#     save_to_io = BytesIO()
#     await message.document.download(destination_file=save_to_io)
#     await message.answer_photo(photo=types.InputFile(save_to_io))






