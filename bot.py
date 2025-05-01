import telebot
import requests

TOKEN = '7505752036:AAGYB1DUL7ZP5wO7RlR5YYbArf-yl_5ur3s'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! برای دیدن قیمت بیت‌کوین دستور /price رو بزن 😊")

@bot.message_handler(commands=['price'])
def send_price(message):
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()  # بررسی وضعیت HTTP
        data = response.json()
        price = data['data']['priceUsd']
        bot.reply_to(message, f"Bitcoin Price (Coincap): ${float(price):,.2f}")
    except Exception as e:
        bot.reply_to(message, f"Error fetching price. Try again later.\n{e}")

print("ربات روشنه")
bot.polling()
