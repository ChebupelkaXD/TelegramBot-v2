from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import scenario
import markups as mark

from time import sleep as sl

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

f = list(open ('TextScenario.txt', encoding = 'Windows-1251'))

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
	
	#Отправляет текст предыстории
	await bot.send_message(message.chat.id, scenario.nachalo)
	sl(1)
	
	#Отпраляет первые 5 строк из файла последовательно
	for i, line in enumerate(f):
		if i < 5:
			await bot.send_message(message.chat.id, line )
			sl(1)

	await bot.send_message(message.chat.id, "Бесполезный кусок говна, все давно сдохли, на что я надеюсь…", reply_markup=mark.button1)
	sl(1)


@dp.callback_query_handler(text_startswith="first_")
async def call_back1(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)
	if call.data  == "first_answer1":
		await bot.send_message(call.from_user.id, "Твою мать!  Эта штука работает!")

	elif call.data == "first_answer2":
		await bot.send_message(call.from_user.id, "Твою мать! До этого момента я был атеистом, но сейчас я действительно уверовал!")

	for i, line in enumerate(f):
			if i > 4 and i < 7:
				await bot.send_message(call.message.chat.id, line )
				sl(1)
	await bot.send_message(call.message.chat.id, "Как думаешь, это считается мародерством?", reply_markup=mark.button2)
	sl(1)


@dp.callback_query_handler(text_startswith="second_")
async def call_back1(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)
	if call.data  == "second_answer3":
		await bot.send_message(call.from_user.id, "Да, прости, где мои манеры")

	elif call.data == "second_answer4":
		await bot.send_message(call.from_user.id, "Ад давно уже на земле…")

	
	for i, line in enumerate(f):
			if i == 7:
				await bot.send_message(call.message.chat.id, line )
				sl(1)


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates = True)
