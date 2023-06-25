import logging

from aiogram import Bot, Dispatcher, executor, types
from sontopbot import chekword
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

API_TOKEN = '6265798683:AAF_wd_UiJhAYoeHj3wZ7sjn5xZjyNPobyw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
telnomer = KeyboardButton("telefoningizni kiriting", request_contact=True)
soz = KeyboardButton("so'z")
matn= KeyboardButton("matn")
boshlash = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
boshlash.add(telnomer)
boshlash1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
boshlash1.row(soz,matn)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("salom\nbu bot @uchiha_javohir tomonidan yaratilgan\nishga tushishimdan oldin nomeringizni yuborishingizni so'rab qolardim", reply_markup=boshlash)

@dp.message_handler(content_types=['contact'])
async def send_welcome1(message: types.Message):
    await message.answer("unay bo'lsa bo'limni tanlang",reply_markup=boshlash1 )

@dp.message_handler(text_contains="so'z")
async def nomadir(message: types.Message):
    await message.reply("so'zni yozing")

@dp.message_handler(text_contains="matn")
async def matn(message: types.Message):
    await message.reply("matni yozing")

@dp.message_handler()
async def echo(message: types.Message):
    words = message.text.split()
    for word in words:
        true_words = ''
        res = chekword(word)
        if res['ok']:
            await message.answer(f"✅{word}")
        else:
            true_words += f"❌{word}\n"
            for text in res ['matches'] :
                true_words += f"✅{text}\n"
            await message.answer(true_words)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
