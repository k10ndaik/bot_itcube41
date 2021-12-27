from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Об IT-CUBE")
b2 = KeyboardButton("направления IT-CUBE")
b3 = KeyboardButton("записаться в IT-CUBE")
b4 = KeyboardButton("КОНТАКТЫ")
b5 = KeyboardButton("Где мы находимся")

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_kb.add(b1).row(b2,b3).row(b4,b5)


