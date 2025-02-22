import json


def load_products():
    with open("database/products.json", "r", encoding="utf-8") as file:
        return json.load(file)

def register_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == "📦 Каталог товарів")
    def send_catalog(message):
        products = load_products()
        for product in products:
            bot.send_photo(
                message.chat.id,
                product["photo"],
                caption=f'🛍 {product["name"]}\n💰 Цена: {product["price"]} грн.\n📄 {product["description"]}'
            )
