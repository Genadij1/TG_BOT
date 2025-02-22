import telebot
from config import TOKEN
from handlers import start, catalog, help, manager, messages, commands, buttons

bot = telebot.TeleBot(TOKEN)


# Подключаем обработчики
start.register_handlers(bot)
catalog.register_handlers(bot)
help.register_handlers(bot)
manager.register_handlers(bot)
messages.register_message_handler(bot)
commands.register_command_handler(bot)
buttons.register_button_handler(bot)


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
