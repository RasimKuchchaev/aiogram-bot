from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import allowed_users
from loader import dp

@dp.inline_handler(text="")
async def emply_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="unknown",
                title="Введите какой-нибудь запрос",
                input_message_content=types.InputTextMessageContent(
                    message_text="Не обязательно жать на кнопку"
                ))
        ],
        cache_time=5
    )

@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_users:
        await query.answer(
            results=[],
            switch_pm_text="Бот не доступен. Подключить бота",
            switch_pm_parameter="connect_user",         # start connect_user
            cache_time=5        # 5 seconds
        )
        return

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="1",
                title="Название которое отображается в инлайн режиме!",
                input_message_content=types.InputTextMessageContent(
                    message_text="Тут какой-то <b>текст</b>, котороый будет отправлен при нажатие на кнопку"
                         ),
                url="https://core.telegram.org/bots/api#inlinequeryresult",
                thumb_url="https://underwriter.gr/wp-content/uploads/2016/03/eias.jpg",
                description="описание инлайн режима"
            ),
            types.InlineQueryResultVideo(
                id="4",
                video_url="https://samplelib.com/lib/preview/mp4/sample-5s.mp4",
                caption="Подпись к видео",
                title="Какое-то видео",
                description="Какое-то описание",
                thumb_url="https://www.aiseesoft.com/images/mac-video-converter-ultimate/convert-video-to-mp4-format.jpg",
                mime_type="video/mp4"
            ),
            types.InlineQueryResultCachedPhoto(
                id="2",
                photo_file_id="AgACAgIAAxkBAAIER2Pn52Wa76eSx0vVoJLlub2LsF7wAALlwDEbIJpAS4cgKeFNGPRkAQADAgADeQADLgQ",
                caption="Какое-то фото",
                title="Какое-то фото",
                description="Какое-то описание"
            ),
        ]
   )

@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer(
        "Вы подключены",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                InlineKeyboardButton(text="Войти в инлайн режим",
                                     switch_inline_query_current_chat="Запрос")
                ]
            ]
        )
    )

