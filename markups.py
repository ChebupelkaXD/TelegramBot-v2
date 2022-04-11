from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

background = InlineKeyboardMarkup(row_width = 2)
Yes = InlineKeyboardButton("Да", callback_data= "answer_yes")
No  = InlineKeyboardButton("Нет", callback_data= "answer_no")

background.add(Yes, No)

button1 = InlineKeyboardMarkup(row_width = 1)
item1 = InlineKeyboardButton("Прием? Кто это?!", callback_data= "first_answer1")
item2 = InlineKeyboardButton("Поздравляю, на связи всевышний", callback_data= "first_answer2")

button1.add(item1, item2)

button2 = InlineKeyboardMarkup(row_width = 1)
item3 = InlineKeyboardButton("Ты так и не представился…", callback_data= "second_answer3")
item4 = InlineKeyboardButton("Для тебя будет отдельное место в аду", callback_data= "second_answer4")

button2.add(item3, item4)

button3 = InlineKeyboardMarkup(row_width = 1)
item5 = InlineKeyboardButton("Называй меня “хозяин” – не ошибешься.", callback_data= "third_answer5")
item6 = InlineKeyboardButton("<Ваше имя>", callback_data= "third_answer6")

button3.add(item5, item6)