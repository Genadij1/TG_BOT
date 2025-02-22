from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_keyboard.add(KeyboardButton("📦 Каталог товарів"))
    menu_keyboard.add(KeyboardButton("❓ Часті питання"))
    menu_keyboard.add(KeyboardButton("📩 Зв`язок з менеджером"))
    return menu_keyboard
