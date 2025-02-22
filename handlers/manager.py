def register_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == "📩 Зв`язок з менеджером")
    def send_faq(message):
        bot.send_message(
            message.chat.id,
            "👩‍💼 <b>Менеджери нашого магазину:</b>",
            parse_mode="HTML"

        )

        bot.send_message(
            message.chat.id,
            "📌 <b>Соломія:</b> <a href='https://t.me/sssssolomiya'>@sssssolomiya</a>",
            parse_mode="HTML"
        )

        bot.send_message(
            message.chat.id,
            "📌 <b>Тетяна:</b> <a href='https://t.me/kmtati'>@kmtati</a>",
            parse_mode="HTML"
        )


