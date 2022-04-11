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

	await bot.send_message(message.chat.id, "*Хотите узнать предысторию событий?*", parse_mode= 'Markdown', reply_markup=mark.background)
	sl(1)

@dp.callback_query_handler(text_startswith="answer_")
async def call_back(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id) #Удаляет кнопки после нажатия
	if call.data  == "answer_yes":
		await bot.send_message(call.from_user.id, scenario.nachalo)

	elif call.data == "answer_no":
		pass
	
	
	#Отпраляет первые 5 строк из файла последовательно
	for i, line in enumerate(f):
		if i < 5:
			await bot.send_message(call.message.chat.id, line )
			sl(1)

	await bot.send_message(call.from_user.id, "Бесполезный кусок говна, все давно сдохли, на что я надеюсь…", reply_markup=mark.button1)
	sl(1)


@dp.callback_query_handler(text_startswith="first_")
async def call_back1(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id) #Удаляет кнопки после нажатия
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
async def call_back2(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)
	if call.data  == "second_answer3":
		await bot.send_message(call.from_user.id, "Да, прости, где мои манеры")

	elif call.data == "second_answer4":
		await bot.send_message(call.from_user.id, "Ад давно уже на земле…")

	
	for i, line in enumerate(f):
			if i == 7:
				await bot.send_message(call.message.chat.id, line )
				sl(1)

	await bot.send_message(call.message.chat.id, "А у тебя какое погоняло?", reply_markup=mark.button3)
	sl(1)

@dp.callback_query_handler(text_startswith="third_")
async def call_back3(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)
	if call.data  == "third_answer5":
		await bot.send_message(call.from_user.id, "…")

	elif call.data == "third_answer6":
		await bot.send_message(call.from_user.id, "Будем знакомы, " + (call.from_user.first_name))

	for i, line in enumerate(f):
		if i > 7 and i < 10:
			await bot.send_message(call.message.chat.id, line )
			sl(1)


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates = True)
