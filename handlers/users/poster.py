from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, bot
from states.poster_state import NewPost


@dp.message_handler(Command("create_post"))
async def create_post(message: types.Message):
    await message.answer("Отправьте мне текст поста на публикацию")
    await NewPost.EnterMessage.set()


@dp.message_handler(state=NewPost.EnterMessage)
async def enter_message(message: types.Message, state:FSMContext):
    # await state.update_data()  # сохраняем машину состояния
    # ссылка на пользователя mention=message.from_user.get_mention()
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention(as_html=True))
    await message.answer("Вы собираетесь отправит пост на проверку?",
                         reply_markup=confirmation_keyboard)
    # await NewPost.Comfirm
    await NewPost.next()    # Отправляем пользователя в статус ожидания


@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Comfirm)
async def confirm_post(call:CallbackQuery, state:FSMContext):
    # Достаем данные из машины состояния
    async with state.proxy() as date:
        text = date.get("text")
        mention = date.get("mention")
    await state.finish()    # Закрываю пользователя
    await call.message.edit_reply_markup()
    await call.message.answer("Вы отправили пост на проверку")

    await bot.send_message(chat_id=ADMINS[0], text=f"Пользователь {mention} хочет сделать пость:")
    await bot.send_message(chat_id=ADMINS[0], text=text, reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Comfirm)
async def cancel_post(call:CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Вы отклонили пост")


# если пользователь в состояние ожидания начнет нажимат на разные кнопки
@dp.message_handler(state=NewPost.Comfirm)
async def _post_unknown(message: types.Message):
    await message.answer("Выберите опубликовать или отклонить пост")


# Admin одобрил пост
@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
    await call.answer("Вы одобрили этот пост", show_alert=True)     # show_alert=True кнопка ОК
    targer_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=targer_channel)     # Отпраляет коппию сообщения

# Admin отклонил пост
@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    await call.answer("Вы отклонили пост.", show_alert=True)
    await call.message.edit_reply_markup()