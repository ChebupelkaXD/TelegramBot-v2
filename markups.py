from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button1 = InlineKeyboardMarkup(row_width = 1)
item1 = InlineKeyboardButton(text = "Прием? Кто это?!", callback_data= "first_answer1")
item2 = InlineKeyboardButton(text = "Поздравляю, на связи всевышний", callback_data= "first_answer2")

button1.add(item1, item2)

button2 = InlineKeyboardMarkup(row_width = 1)
item3 = InlineKeyboardButton("Ты так и не представился…", callback_data= "second_answer3")
item4 = InlineKeyboardButton("Для тебя будет отдельное место в аду", callback_data= "second_answer4")

button2.add(item3, item4)