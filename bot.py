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
def send_db_content(message):
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.chat.id, "⛔ У вас нет доступа к этой команде!")
        return
    
    conn = sqlite3.connect("database.db")  # Подключаемся к БД
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages ORDER BY id DESC LIMIT 10;")  # Берём 10 последних записей
    data = cursor.fetchall()
    conn.close()  # Закрываем соединение

    if data:
        text = "\n".join([str(row) for row in data])  # Преобразуем данные в текст
        bot.send_message(message.chat.id, f"📊 Последние записи в БД:\n{text}")
    else:
        bot.send_message(message.chat.id, "📭 База данных пуста.")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
