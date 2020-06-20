"""Сервер Telegram бота"""
import logging
from aiogram import Bot, Dispatcher, executor, types
from misc import bot_config


API_TOKEN = bot_config['token']

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def auth(func):

    async def wrapper(message):
        if message['from']['id'] != 121212121:
            return await message.reply('Access Denied', reply=False)
        return await func(message)
    return wrapper


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        'Бот для получения обменного курса тенге\n\n'
        'Лучшая покупка USD: /usd_best\n',
        reply=False
    )

@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cat01.png', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here')

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
