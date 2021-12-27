from aiogram.utils import executor
#импортируем executor
from bot import dp
#импортируем диспчер
from menu.default_menu import set_default_commands
#мпортируем описания стандартного меню
from handlers.client import client
#импортируем хендлеры клиента

async def on_startup(dp):
    await set_default_commands(dp)
#создаем функцию с нужным набором функционала

from aiogram import types

client(dp)


executor.start_polling(dp, on_startup=on_startup)
#Запускаем диспачер и функционал