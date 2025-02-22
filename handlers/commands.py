import telebot
from database.db import save_action

def register_command_handler(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start', 'help'])
    def handle_command(message):
        user_id = message.chat.id
        username = message.from_user.username if message.from_user.username else "Неизвестный"
        command = message.text

        print(f"⚡ Команда: {username} -> {command}")

        # Сохраняем в БД
        save_action(user_id, username, "команда", command)

        if command == "/start":
            bot.send_message(user_id, "Привет! Я бот T&S_flow. Чем могу помочь?")
        elif command == "/help":
            bot.send_message(user_id, "Список доступных команд: /start, /help")
