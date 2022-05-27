from aiogram import Bot, types, asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor, exceptions
from aiogram.utils.markdown import hlink
import config
import scenario
import markups as mark
from time import sleep as sl


from config import TOKEN, YOOTOKEN

ytoken = YOOTOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

f = list(open ('TextScenario.txt', encoding = 'Windows-1251'))
a = list(open ('Answers.txt', encoding = 'Windows-1251'))
photo = open('YOU DIED.jpg', 'rb')
leo = open('DiCaprio.jpg', 'rb')


@dp.message_handler(commands = ['menu'])
async def menu(message: types.Message):
	await bot.send_message(message.chat.id, "Спомощью меню, вы можете отправить донат или связаться с технической поддержкой.", reply_markup = mark.Menu)

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
	await bot.send_message(message.chat.id, "*Хотите узнать предысторию событий?*", parse_mode= 'Markdown', reply_markup=mark.background)
	sl(1)

#-------------V-БЛОК ДОНАТА-V------------

@dp.message_handler()
async def bot_message(message: types.Message):
	if message.text == 'Чашечка кофе для авторов☕':
		await bot.send_invoice(message.chat.id, title ="Чашечка кофе для авторов☕", description = "Наша команда очень старалась сделать что-то интересное и увлекательное для вас. Мы будем рады, даже небольшой чашечке кофе, если вам понравилась наша игра ❤", payload = "Чашечка кофе☕", provider_token = ytoken, currency="rub", photo_url = 'https://srisovki.one/wp-content/uploads/2021/05/image_562404190714424312763-768x834.jpg', photo_height=512, photo_width=512, photo_size=512, start_parameter = "test_pay", prices = [{"label": "Мани-мани", "amount": 7000}])
	
	if message.text == 'Связь с админом👨‍💻':
		await message.answer('<a href="https://t.me/vuorg">Обкашлять пару вопросиков</a>', parse_mode=types.ParseMode.HTML)

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
	await bot.answer_pre_checkout_query(pre_checkout_query.id, ok = True)

@dp.message_handler(content_types=['successful_payment'])
async def process_successful_payment(message: types.Message):
	if message.successful_payment.invoice_payload == "Чашечка кофе☕":
		await bot.send_photo(message.from_user.id, text="Чтобы продолжить игру, нажмите на кнопку ответа Ярику.", photo = leo)

#--------------V-БЛОК ИГРЫ-V------------

@dp.callback_query_handler(text_startswith="answer_")
async def call_back(call: types.CallbackQuery):
	
	await bot.delete_message(call.from_user.id, call.message.message_id) #Удаляет кнопки после нажатия
	if call.data  == "answer_yes":
		await bot.send_message(call.from_user.id, scenario.nachalo)

	elif call.data == "answer_no":
		pass

	await bot.send_message(call.message.chat.id, '****Установка соединения****' )
	sl(3)
	await bot.send_message(call.message.chat.id, '****Звук скрежета помех радиостанции****' )
	sl(3)

	for i, line in enumerate(f):
		if i < 7:
			orig_text = line
			msg = await bot.send_message(call.from_user.id, 'I')
			sl(0.1)
			tbp = orig_text[:1]
			for x in orig_text[1:]:
				try:
					await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
					sl(0.1)
					tbp += x
					await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

				except exceptions.RetryAfter as e:
					await asyncio.sleep(e.timeout)
			sl(2)

	await bot.send_message(call.from_user.id, "Все давно сдохли, на что я надеюсь…", reply_markup=mark.button1)
	sl(2)


@dp.callback_query_handler(text_startswith="first_")
async def call_back1(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id) #Удаляет кнопки после нажатия
	if call.data  == "first_answer1":
		
		orig_text = "Твою мать!  Эта штука работает!"
		msg = await bot.send_message(call.from_user.id, 'I')
		sl(0.1)
		tbp = orig_text[:1]
		for x in orig_text[1:]:
			try:
				await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
				sl(0.1)
				tbp += x
				await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

			except exceptions.RetryAfter as e:
				await asyncio.sleep(e.timeout)
		sl(2)

	elif call.data == "first_answer2":
	
		orig_text =  "Боже, я уверовал!"
		msg = await bot.send_message(call.from_user.id, 'I')
		sl(0.1)
		tbp = orig_text[:1]
		for x in orig_text[1:]:
			try:
				await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
				sl(0.1)
				tbp += x
				await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

			except exceptions.RetryAfter as e:
				await asyncio.sleep(e.timeout)
		sl(2)

	for i, line in enumerate(f):
		if i > 7 and i < 14:
			orig_text = line
			msg = await bot.send_message(call.from_user.id, 'I')
			sl(0.1)
			tbp = orig_text[:1]
			for x in orig_text[1:]:
				try:
					await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
					sl(0.1)
					tbp += x
					await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

				except exceptions.RetryAfter as e:
					await asyncio.sleep(e.timeout)
			sl(2)

	await bot.send_message(call.message.chat.id, "Хоть с кем-то…", reply_markup=mark.button2)
	sl(2)


@dp.callback_query_handler(text_startswith="second_")
async def call_back2(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)
	if call.data  == "second_answer3" or call.data == "second_answer4":
	
		for i, line in enumerate(f):
			if i > 14 and i < 25:
				orig_text = line
				msg = await bot.send_message(call.from_user.id, 'I')
				sl(0.1)
				tbp = orig_text[:1]
				for x in orig_text[1:]:
					try:
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
						sl(0.1)
						tbp += x
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

					except exceptions.RetryAfter as e:
						await asyncio.sleep(e.timeout)
				sl(2)

		await bot.send_message(call.message.chat.id, "Как у тебя обстановка?", reply_markup=mark.button3)
		sl(2)

@dp.callback_query_handler(text_startswith="third_")
async def call_back3(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)

	if call.data  == "third_answer5":

		orig_text = "Что значит «Как и всегда»?"
		msg = await bot.send_message(call.from_user.id, 'I')
		sl(0.1)
		tbp = orig_text[:1]
		for x in orig_text[1:]:
			try:
				await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
				sl(0.1)
				tbp += x
				await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

			except exceptions.RetryAfter as e:
				await asyncio.sleep(e.timeout)
		sl(2)

	if call.data  == "third_answer6":

		for i, line in enumerate(a):
			if i > 0 and i < 3:
				orig_text = line
				msg = await bot.send_message(call.from_user.id, 'I')
				sl(0.1)
				tbp = orig_text[:1]
				for x in orig_text[1:]:
					try:
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
						sl(0.1)
						tbp += x
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

					except exceptions.RetryAfter as e:
						await asyncio.sleep(e.timeout)
				sl(2)

	await bot.send_message(call.message.chat.id, "Где ты был последнюю неделю?", reply_markup=mark.button4)
	sl(2)

@dp.callback_query_handler(text_startswith="fourth_")
async def call_back3(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)
	if call.data  == "fourth_answer7" or  call.data == "fourth_answer8":
		
		for i, line in enumerate(f):
			if i > 25 and i < 92:
				orig_text = line
				msg = await bot.send_message(call.from_user.id, 'I')
				sl(0.1)
				tbp = orig_text[:1]
				for x in orig_text[1:]:
					try:
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
						sl(0.1)
						tbp += x
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

					except exceptions.RetryAfter as e:
						await asyncio.sleep(e.timeout)
				sl(2)

		await bot.send_message(call.message.chat.id, "Да и воды почти не осталось", reply_markup=mark.button5)
		sl(2)

@dp.callback_query_handler(text_startswith="fifth_")
async def call_back3(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)
	if call.data  == "fifth_answer9":

		for i, line in enumerate(a):
			if i > 4 and i < 34:
				orig_text = line
				msg = await bot.send_message(call.from_user.id, 'I')
				sl(0.1)
				tbp = orig_text[:1]
				for x in orig_text[1:]:
					try:
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
						sl(0.1)
						tbp += x
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

					except exceptions.RetryAfter as e:
						await asyncio.sleep(e.timeout)
				sl(2)

	game_over=0
	if call.data  == "fifth_answer10":

		game_over=1

		for i, line in enumerate(a):
			if i > 34 and i < 65:
				orig_text = line
				msg = await bot.send_message(call.from_user.id, 'I')
				sl(0.1)
				tbp = orig_text[:1]
				for x in orig_text[1:]:
					try:
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=f'{tbp}|')
						sl(0.1)
						tbp += x
						await bot.edit_message_text(chat_id=call.from_user.id, message_id=msg.message_id, text=tbp)

					except exceptions.RetryAfter as e:
						await asyncio.sleep(e.timeout)
				sl(2)

		await bot.send_message(call.message.chat.id, "***Связь потеряна***")
		sl(2)

		await bot.send_photo(call.message.chat.id, photo )
		sl(2)

		await bot.send_message(call.message.chat.id, "Чтобы начать игру зановго, нажмите на /start")


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates = True)
