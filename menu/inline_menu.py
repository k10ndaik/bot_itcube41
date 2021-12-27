from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_inline_b1 = InlineKeyboardButton(text="Об IT-CUBE", callback_data="about_menu_inline")
menu_inline_b2 = InlineKeyboardButton(text="направления IT-CUBE", callback_data="direction")
menu_inline_b3 = InlineKeyboardButton(text="записаться в IT-CUBE", callback_data="sign up")
menu_inline_b4 = InlineKeyboardButton(text="КОНТАКТЫ", callback_data="contact")
menu_inline_b5 = InlineKeyboardButton(text="Где мы находимся", url="https://2gis.ru/p_kamchatskiy/firm/70000001055358127?m=158.642585%2C53.072924%2F17")

menu_inline = InlineKeyboardMarkup(row_width=1)
menu_inline.add(menu_inline_b1, menu_inline_b2, menu_inline_b3, menu_inline_b4, menu_inline_b5)

about_menu_inline_b1 = InlineKeyboardButton(text="Сайт IT-CUBE", url="https://itcube41.ru/")
about_menu_inline_b2 = InlineKeyboardButton(text="Instagram IT-CUBE", url="https://www.instagram.com/itcube41/")
about_menu_inline_b3 = InlineKeyboardButton(text="YouTube IT-CUBE", url="https://www.youtube.com/channel/UCd1ZVyz-GFrUIWOU4d7R17w")
about_menu_inline_b4 = InlineKeyboardButton(text="TikTok IT-CUBE", url="https://www.tiktok.com/@itcube41?lang=ru-RU&is_copy_url=1&is_from_webapp=v1")
about_menu_inline_b5 = InlineKeyboardButton(text="назад", callback_data="back1")

about_menu_inline = InlineKeyboardMarkup(row_width=1)
about_menu_inline.add(about_menu_inline_b1, about_menu_inline_b2,
                      about_menu_inline_b3, about_menu_inline_b4, about_menu_inline_b5)

direction_inline_b1 = InlineKeyboardButton(text="Java", url="https://itcube41.ru/java-programming/")
direction_inline_b2 = InlineKeyboardButton(text="Python", url="https://itcube41.ru/python-programming/")
direction_inline_b3 = InlineKeyboardButton(text="VR", url="https://itcube41.ru/development-of-virtual-and-augmented-reality/")
direction_inline_b4 = InlineKeyboardButton(text="Мобильная разработка", url="https://itcube41.ru/mobile-development/")
direction_inline_b5 = InlineKeyboardButton(text="Роботы", url="https://itcube41.ru/robot-programming/")
direction_inline_b6 = InlineKeyboardButton(text="Системное администрирование", url="https://itcube41.ru/system-administration/")
direction_inline_b7 = InlineKeyboardButton(text="назад", callback_data="back1")

direction_menu_inline = InlineKeyboardMarkup(row_width=1)
direction_menu_inline.add(direction_inline_b1, direction_inline_b2, direction_inline_b3,
                          direction_inline_b4, direction_inline_b5, direction_inline_b6,direction_inline_b7)

sign_up_menu_inline_b1 = InlineKeyboardButton(text="Видеоинструкция", url="https://www.youtube.com/watch?v=6AldBSCDvQ8")
sign_up_menu_inline_b2 = InlineKeyboardButton(text="Зарегистрироваться в 'НАВИГАТОР'", url="https://dop.sgo41.ru/#registration")
sign_up_menu_inline_b3 = InlineKeyboardButton(text="Заполнить анкету", url="https://docs.google.com/forms/d/1cOvLwjXX05XpWTJ-APBlC9R0UfPVxV-qD_fELVxOAHo/viewform?edit_requested=true")
sign_up_menu_inline_b4 = InlineKeyboardButton(text="назад", callback_data="back1")

sign_up_menu = InlineKeyboardMarkup(row_width=1)
sign_up_menu.add(sign_up_menu_inline_b1,sign_up_menu_inline_b2,sign_up_menu_inline_b3,sign_up_menu_inline_b4)

