from flask import Flask
import threading
import bot 

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running ❤️"

def run_bot():
    bot.main()

if __name__ == "__main__":
    t = threading.Thread(target=run_bot)
    t.start()
    app.run(host="0.0.0.0", port=10000)
