from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import scenario
import markups as mark
from time import sleep as sl

from config import TOKEN, YOOTOKEN

ytoken = YOOTOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

f = list(open ('TextScenario.txt', encoding = 'Windows-1251'))
photo = open('YOU DIED.jpg', 'rb')
leo = open('DiCaprio.jpg', 'rb')


@dp.message_handler(commands = ['menu'])
async def menu(message: types.Message):
	await bot.send_message(message.chat.id, "Спомощью меню, вы можете отправиь донат или связаться с технической поддержкой.", reply_markup = mark.Menu)

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
	await bot.send_message(message.chat.id, "*Хотите узнать предысторию событий?*", parse_mode= 'Markdown', reply_markup=mark.background)
	sl(1)

@dp.message_handler()
async def bot_message(message: types.Message):
	if message.text == 'Чашечка кофе для авторов☕':
		await bot.send_invoice(message.chat.id, title ="Чашечка кофе для авторов☕", description = "Наша команда очень старалась сделать что-то интересное и увлекательное для вас. Мы будем рады, даже не большой чашечке кофе, если вам понравилась наша игра ❤", payload = "Чашечка кофе☕", provider_token = ytoken, currency="rub", photo_url = 'https://srisovki.one/wp-content/uploads/2021/05/image_562404190714424312763-768x834.jpg', photo_height=512, photo_width=512, photo_size=512, start_parameter = "test_pay", prices = [{"label": "Мани-мани", "amount": 7000}])

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
	await bot.answer_pre_checkout_query(pre_checkout_query.id, ok = True)

@dp.message_handler(content_types=['successful_payment'])
async def process_successful_payment(message: types.Message):
	if message.successful_payment.invoice_payload == "Чашечка кофе☕":
		await bot.send_photo(message.from_user.id, text="Чтобы продолжить игру, нажмите на кнопку ответа Ярику.", photo = leo)


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

	go = 0 # GAME OVER
	if go != 1 and call.data  == "third_answer5":
		go = 1
		await bot.send_message(call.from_user.id, "Пойду вскроюсь...")
		sl(1)
		await bot.send_message(call.from_user.id, "***Ярик посчитал, что лучше умереть, чем жить в мире с таким арбузером, как Вы.***")
		sl(1)
		await bot.send_photo(call.from_user.id, photo = photo)
		sl(1)
		await bot.send_message(call.from_user.id, "Чтобы начать игру занаво, выберете команду /start")


	elif go != 1 and call.data == "third_answer6":
		await bot.send_message(call.from_user.id, "Будем знакомы, " + (call.from_user.first_name)) # (call.from_user.first_name) - вставляет в сообщение бота ник пользователя
	
	if go != 1:
		for i, line in enumerate(f):
			if i > 7 and i < 10:
				await bot.send_message(call.message.chat.id, line )
				sl(1)

		await bot.send_message(call.message.chat.id, "Твою мать, чуть не откинулся…", reply_markup=mark.button4)
		sl(1)

@dp.callback_query_handler(text_startswith="fourth_")
async def call_back3(call: types.CallbackQuery):
	await bot.delete_message(call.from_user.id, call.message.message_id)
	if call.data  == "fourth_answer7":
		await bot.send_message(call.from_user.id, "Привитый. Мне повезло получить иммунитет после инъекции. Но, к сожалению, не без последствий. Легким п#зд@...\n"
												  +"Сейчас у меня вряд ли получится бегать марафоны. Поэтому надо держать подальше от зараженных. "
												  +"Некоторые из них бегают очень быстро…")

	elif call.data == "fourth_answer8":
		await bot.send_message(call.from_user.id, "Не сглазь!\n"
												  +"Хорошо, что мне повезло получить иммунитет после инъекции. Но, к сожалению, не без последствий. Легким п#зд@...\n"
												  +"Сейчас у меня вряд ли получится бегать марафоны. Поэтому надо держаться подальше от зараженных. Некоторые из них передвигаются очень быстро…")




if __name__ == "__main__":
	executor.start_polling(dp, skip_updates = True)
