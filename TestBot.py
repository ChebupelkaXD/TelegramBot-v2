from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor, exceptions
import config
import scenario
import markups as mark

from time import sleep as sl

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

f = list(open ('TextScenario.txt', encoding = 'Windows-1251'))

'''
@dp.message_handler(commands=['start'])
async def stats(govno):
	await bot.send_message(govno.chat.id, "Текст для теста")
'''


'''
@dp.message_handler()
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

@dp.message_handler(commands = ['start'])
async def type(message):
    orig_text = "Текст для теста"
    text = orig_text
    tbp = "" 
    typing_symbol = "|"
    await bot.send_message(message.chat.id, orig_text[:1])
 
    while(tbp != orig_text):

        await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text = tbp + typing_symbol)
        sleep(0.05)
 
        tbp = tbp + text[0]
        text = text[1:]
 
        await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text = tbp)
        sleep(0.05)
 
        


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates = True)