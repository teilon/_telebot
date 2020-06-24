"""Сервер Telegram бота, запускаемый непосредственно"""
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
import exceptions
from misc import bot_config
from meth import get_stat

logging.basicConfig(level=logging.INFO)

API_TOKEN = bot_config['token']
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Отправляет приветственное сообщение и помощь по боту"""
    await message.reply(
        'Бот для получения обменного курса тенге\n\n'
        'Лучшая покупка USD: /usd\n'
        'Лучшая покупка RUB: /rub\n'
        'Лучшая покупка EUR: /eur\n',
        reply=False)


@dp.message_handler(commands=['usd'])
async def today_statistics(message: types.Message):
    """покупка USD"""
    answer = get_stat('USD')
    await message.answer(answer)


@dp.message_handler(commands=['rub'])
async def month_statistics(message: types.Message):
    """покупка RUB"""
    answer = get_stat('RUB')
    await message.answer(answer)


@dp.message_handler(commands=['eur'])
async def list_expenses(message: types.Message):
    """покупка EUR"""
    answer = get_stat('EUR')
    await message.answer(answer)

@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cat01.png', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)