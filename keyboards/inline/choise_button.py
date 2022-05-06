from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                [
                                  InlineKeyboardButton(
                                      text="Купить грушу",
                                      callback_data=buy_callback.new(item_name="peer",
                                                                     quantity=1)
                                  ),
                                  InlineKeyboardButton(
                                      text="Купить яблоки",
                                      callback_data="buy:apple:5"
                                  )
                                ],
                                [
                                  InlineKeyboardButton(
                                      text="Отмена",
                                      callback_data="cancel"
                                  )
                                ]
                              ])


pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = "https://core.telegram.org/bots/api#inlinekeyboardbutton"

pear_link = InlineKeyboardButton(text="Купи тут", url=PEAR_LINK)

pear_keyboard.insert(pear_link)