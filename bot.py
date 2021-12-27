#файл бота itCube41_bot
from aiogram import Bot
#загружаем класс бота
from setup import token
#импортируем токен
from aiogram.dispatcher import Dispatcher
#импортируем класс диспечер

#from aiogram.contrib.fsm_storage.memory import MemoryStorage
#импортируем класс памяти для храниея данных состояния машины


bot = Bot(token)
#создаем объект класса Bot, прописываем токен бота
dp = Dispatcher(bot)
#создаем объект класса Dispatcher, указываем бота для работы диспачера