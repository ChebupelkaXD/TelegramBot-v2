from aiogram import Bot, types, asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor, exceptions
import config
import scenario
import markups as mark

from time import sleep as sl

from config import TOKEN, YOOTOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#f = list(open ('TextScenario.txt', encoding = 'Windows-1251'))
#photo = open('YOU DIED.jpg', 'rb')

@dp.message_handler(commands = ['start'])
async def choice_effect(mes):

    choice_button=InlineKeyboardMarkup(row_width = 1)
    One = InlineKeyboardButton("Начать выполнение кода из второго bot.py", callback_data= "choice_one")
    choice_button.add(One)

    await bot.send_message(mes.chat.id, "Нажмите на кнопку для запуска файла bot.py", reply_markup = choice_button)

@dp.callback_query_handler(text_startswith="choice_")
async def call_back0(call: types.CallbackQuery):

    if call.data == 'choice_one':
        #После выполнения условия должен выполняться код из bot.py

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates = True)

'''
@dp.message_handler(commands = ['start'])
async def effect(mes):
    orig_text = scenario.nachalo
    msg = await bot.send_message(mes.chat.id, 'I')
    tbp = orig_text[:1]
    for x in orig_text[1:]:
        try:
            await bot.edit_message_text(chat_id=mes.chat.id, message_id=msg.message_id, text=f'{tbp}|')
            sl(0.01)
            tbp += x
            await bot.edit_message_text(chat_id=mes.chat.id, message_id=msg.message_id, text=tbp)

        except exceptions.RetryAfter as e:
            await asyncio.sleep(e.timeout)
'''
'''
@dp.message_handler(commands = ['start'])
async def hueta(message):
	try:
		mes = message.text
		await bot.send_message(message.chat.id, 'ВЗЛОМ ' + str(mes))
		msg = await bot.send_message(message.chat.id, '1%')
		for i in range(2, 101):
			await bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=str(i) + '%')
			sl(1)
		await bot.send_message(message.chat.id, 'УСПЕШНО ВЗЛОМАНО ' + str(mes) + """. ВАМ ДОСТУПНЫ ПРАВА АДМИНИСТРАТОРА/МОДЕРАТОРА""")
	except IndexError:
		await bot.send_message(message.chat.id, """Что бы симулировать влом чего-то, вам нужно ввести обьект для взлома после команды.""")
'''
'''
@dp.message_handler(commands = ['start'])
async def effect(mes):
    orig_text = 'Текст для тестирования'
    msg = await bot.send_message(call.chat.id, 'I')
    sl(0.5)
    tbp = orig_text[:1]
    for x in orig_text[1:]:
        await bot.edit_message_text(chat_id=call.chat.id, message_id=msg.message_id, text=f'{tbp}|')
        sl(0.5)
        tbp += x
        await bot.edit_message_text(chat_id=call.chat.id, message_id=msg.message_id, text=tbp)

'''
'''
async def effect(mes):
    orig_text = mes
    msg = await bot.send_message(call.chat.id, '|')
    sl(0.5)
    tbp = orig_text[:1]
    for x in orig_text[1:]:
        await bot.edit_message_text(chat_id=call.chat.id, message_id=msg.message_id, text=f'{tbp}|')
        sl(0.5)
        tbp += x
        await bot.edit_message_text(chat_id=call.chat.id, message_id=msg.message_id, text=tbp)
'''
'''
def effect(mes):
    orig_text = mes
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):

            tbp += typing_symbol
            sl(0.5)
 
            tbp = tbp + text[0]
            text = text[1:]
            sl(0.5)

'''
