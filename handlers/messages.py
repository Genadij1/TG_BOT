import telebot

from database.db import save_action


def register_message_handler(bot: telebot.TeleBot):
    @bot.message_handler(func=lambda message: True)  # Ловим все сообщения
    def log_message(message):
        user_id = message.chat.id
        username = message.from_user.username if message.from_user.username else "Неизвестный"
        text = message.text

        print(f"📩 Сообщение от {username}: {text}")

        # Сохраняем в БД
        save_action(user_id, username, "сообщение", text)

        bot.send_message(user_id, "Ваше сообщение сохранено!")
