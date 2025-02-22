import telebot
from database.db import save_action


def register_button_handler(bot: telebot.TeleBot):
    @bot.message_handler(
        func=lambda message: message.text in ["📦 Каталог товаров", "❓ Частые вопросы", "📩 Связаться с менеджером"])
    def handle_button_click(message):
        user_id = message.chat.id
        username = message.from_user.username if message.from_user.username else "Неизвестный"
        button_text = message.text

        print(f"🔘 Нажата кнопка: {username} -> {button_text}")

        # Сохраняем в БД
        save_action(user_id, username, "кнопка", button_text)

        bot.send_message(user_id, f"Вы выбрали: {button_text}")
