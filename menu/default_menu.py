#меню стандартного меню /
from aiogram import types
#импортируем типы

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "открыть меню")
        ]
    )
#функция изменения описания стандарного меню /