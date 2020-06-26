"""Сервер Telegram бота, запускаемый непосредственно"""
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from meth import get_stat

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'show', 'help'])
async def cmd_start(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="USD"))
    poll_keyboard.add(types.KeyboardButton(text="RUB"))
    poll_keyboard.add(types.KeyboardButton(text="EUR"))
    await message.answer(
        'Бот для получения обменного курса тенге',
        reply_markup=poll_keyboard)

# Хэндлер на текстовое сообщение с текстом “USD”
@dp.message_handler(lambda message: message.text in ('USD', 'RUB', 'EUR'))
async def action_cancel(message: types.Message):
    answer = get_stat(message.text)
    await message.answer(answer['buy'])
    await message.answer(answer['sale'])

# --------------

@dp.message_handler(commands=['usd'])
async def today_statistics(message: types.Message):
    """покупка USD"""
    answer = get_stat('USD')
    await message.answer(answer['buy'])
    await message.answer(answer['sale'])

# --------------

@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cat01.png', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here')

# --------------

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)