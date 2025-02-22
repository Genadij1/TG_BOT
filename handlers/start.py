from utils.keyboards import get_main_menu  # Импортируем клавиатуру


def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(
            message.chat.id,
            f'Привіт, {message.from_user.first_name}! Ласкаво просимо у T&S_flow! 🎉',
            reply_markup=get_main_menu()
        )
