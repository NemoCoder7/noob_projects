import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6077529400:AAFebhvB4OLWMhmDeQYBmBiLSVvU-gUnRAc'
wikipedia.set_lang('uz')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm WikiBot!\nCreated by Mirzohidxon.")



@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bu mavzuda maqola mavjud emas')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)