import telebot
import requests

TOKEN = "7505752036:AAHfucAapryCh8-pBHzfIOH2JayvyRlEDR0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام داداش صفا! خوش اومدی به ربات 🫡")

@bot.message_handler(commands=['price'])
def send_price(message):
    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        data = response.json()
        price = data['data']['priceUsd']
        bot.reply_to(message, f"Bitcoin Price (Coincap): ${float(price):,.2f}")
    except Exception as e:
        bot.reply_to(message, "Error fetching price. Try again later.")

bot.infinity_polling()
