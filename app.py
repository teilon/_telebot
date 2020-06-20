"""Сервер Telegram бота, запускаемый непосредственно"""
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
import exceptions
from misc import bot_config


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
    """Лучшая покупка USD"""
    answer_message = 'Лучшая покупка USD'
    await message.answer(answer_message)


@dp.message_handler(commands=['rub'])
async def month_statistics(message: types.Message):
    """Лучшая покупка RUB"""
    answer_message = 'Лучшая покупка RUB'
    await message.answer(answer_message)


@dp.message_handler(commands=['eur'])
async def list_expenses(message: types.Message):
    """Лучшая покупка EUR"""
    answer_message = 'Лучшая покупка EUR'
    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)