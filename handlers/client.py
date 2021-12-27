from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types, Dispatcher
from menu.inline_menu import menu_inline, about_menu_inline, direction_menu_inline,sign_up_menu
from text import about, sing, cont

async def start(message: types.Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAANxYarwiOgWvg10PqslwYKR7Owq3-oAAny5MRuz-1FJrinRpKyH2hgBAAMCAAN5AAMiBA",
        reply_markup=menu_inline)
    await message.delete()

async def about_menu(message: types.CallbackQuery):
    await message.answer(text=about, show_alert=True)
    await message.message.edit_reply_markup(about_menu_inline)

async def back1(message: types.CallbackQuery):
    await message.answer(text="ГЛАВНОЕ МЕНЮ")
    await message.message.edit_reply_markup(menu_inline)

async def direction(message: types.CallbackQuery):
    await message.answer(text="НАПРАВЛЕНИЯ")
    await message.message.edit_reply_markup(direction_menu_inline)

async def sign_up(message: types.CallbackQuery):
    await message.answer(text=sing, show_alert=True)
    await message.answer(text="ЗАПИСАТЬСЯ")
    await message.message.edit_reply_markup(sign_up_menu)

async def contact(message: types.CallbackQuery):
    await message.answer(text=cont, show_alert=True)




def client(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart())
    dp.register_callback_query_handler(about_menu, text="about_menu_inline")
    dp.register_callback_query_handler(back1, text="back1")
    dp.register_callback_query_handler(direction, text="direction")
    dp.register_callback_query_handler(sign_up, text="sign up")
    dp.register_callback_query_handler(contact, text="contact")

