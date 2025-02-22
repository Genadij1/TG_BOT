import sqlite3
import os

# Создаём папку database, если её нет
if not os.path.exists("database"):
    os.makedirs("database")

# Подключаемся к БД
conn = sqlite3.connect("database/messages.db", check_same_thread=False)
cursor = conn.cursor()

# Создаём таблицу (если её нет)
cursor.execute('''
CREATE TABLE IF NOT EXISTS actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    username TEXT,
    action_type TEXT,  -- Тип действия (команда, кнопка, сообщение)
    content TEXT,  -- Текст сообщения, команды или кнопки
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# Функция для сохранения действий пользователя
def save_action(user_id, username, action_type, content):
    try:
        cursor.execute("INSERT INTO actions (user_id, username, action_type, content) VALUES (?, ?, ?, ?)",
                       (user_id, username, action_type, content))
        conn.commit()
        print(f"✅ Действие сохранено: {user_id} | {username} | {action_type} | {content}")
    except Exception as e:
        print(f"❌ Ошибка при сохранении: {e}")
