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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
