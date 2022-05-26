from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


Menu = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
btnDonate = KeyboardButton('Чашечка кофе для авторов☕')
btnSupport = KeyboardButton('Связь с админом👨‍💻')
Menu.add(btnDonate, btnSupport)

background = InlineKeyboardMarkup(row_width = 2)
Yes = InlineKeyboardButton("Да", callback_data= "answer_yes")
No  = InlineKeyboardButton("Нет", callback_data= "answer_no")
background.add(Yes, No)

button1 = InlineKeyboardMarkup(row_width = 1)
item1 = InlineKeyboardButton("Прием? Кто это?!", callback_data= "first_answer1")
item2 = InlineKeyboardButton("Поздравляю, на связи всевышний…", callback_data= "first_answer2")
button1.add(item1, item2)

button2 = InlineKeyboardMarkup(row_width = 1)
item3 = InlineKeyboardButton("Кто ты? ", callback_data= "second_answer3")
item4 = InlineKeyboardButton("Что происходит?", callback_data= "second_answer4")
button2.add(item3, item4)

button3 = InlineKeyboardMarkup(row_width = 1)
item5 = InlineKeyboardButton("Все в порядке. Как и всегда…", callback_data= "third_answer5")
item6 = InlineKeyboardButton("Ты с дурки сбежал?", callback_data= "third_answer6")
button3.add(item5, item6)

button4 = InlineKeyboardMarkup(row_width = 1)
item7 = InlineKeyboardButton("Место, где я нахожусь. Здесь нет интернета…", callback_data= "fourth_answer7")
item8 = InlineKeyboardButton("Я не могу сказать…", callback_data= "fourth_answer8")
button4.add(item7, item8)