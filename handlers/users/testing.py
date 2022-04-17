from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1. \n\n"
                         "Вы часто занимаетесь бесмысленными делами ?")

    await Test.Q1.set()
    # await Test.first()

# состояние ответа на 1 вопрос
@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state=FSMContext):
    answer = message.text

# Сохранение состояния
    await state.update_data(answer1=answer)
    # await state.update_data(
    #     {
    #         "answer1": answer
    #     }
    # )

    await message.answer("Вопрос №2. \n\n"
                          "Ваша память ужудшилась ?")

    # await Test.Q2.set()
    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state=FSMContext):
    # Достаем переменую из машины состояния
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer("Спастбо за ваши ответы")
    await message.answer(f"Ответ 1: {answer1}")
    await message.answer(f"Ответ 2: {answer2}")

# Чтобы все время не оставатся в состояние ответа на вопрос надо сбросит состояние
    await state.finish()
    # await state.reset_state()
    # await state.reset_state(with_data=False)  # сброс состояние не удаляя данные




