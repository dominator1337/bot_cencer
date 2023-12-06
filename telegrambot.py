from collections import defaultdict
from aiogram import Bot, Dispatcher, types, executor
from loadtxt2 import open_txt_file
import time
import logging
import asyncio

list_bad_words = open_txt_file()

TOKEN = "6684024696:AAHjmtb7cDMNXTUT7lvQTW2ZGJyuFQyWIvk"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

user_warning = defaultdict(lambda: 0)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.reply("Привет, я бот. Приятно познакомиться")


@dp.message_handler()
async def message(message: types.Message):
    user_id = message.from_user.id
    user = await bot.get_chat_member(chat_id=message.chat.id, user_id=user_id)
    user_name = user.user.full_name
    text = message.text.lower()
    word_list = text.split()


    if set(word_list) & set(list_bad_words):
        user_warning[user_id] = user_warning[user_id] + 1
        await message.reply(f"{user_name} написал плохое слово, у него {user_warning[user_id]}/3 предупреждений")
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        if user_warning[user_id] >= 3:
            await bot.kick_chat_member(chat_id=message.chat.id, user_id=user_id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
