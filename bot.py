import telebot
import requests

TOKEN = "7505752036:AAHfucAapryCh8-pBHzfIOH2JayvyRlEDR0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hey! I'm your crypto price bot. Send /price to get the latest Bitcoin price!")

@bot.message_handler(commands=['price'])
def send_price(message):
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        data = response.json()
        price = data['bitcoin']['usd']
        bot.reply_to(message, f"Bitcoin Price (Coingecko): ${float(price):,.2f}")
    except Exception as e:
        bot.reply_to(message, "Error fetching price. Try again later.")

bot.polling(non_stop=True)
