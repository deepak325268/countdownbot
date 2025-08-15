import time
import os
from flask import Flask
from telegram import Bot

app = Flask(__name__)

# Railway में environment variables से पढ़ेगा
TOKEN = os.getenv("8219333410:AAFGFPCi0cp6sOrIqEAy7Kzy7BD5yDUZrFg")
CHAT_ID = os.getenv("-1002893041133")
bot = Bot(token=TOKEN)

@app.route("/")
def run_countdown():
    countdown = ["3", "2", "1", "Go!"]
    last_msg_id = None

    for item in countdown:
        msg = bot.send_message(chat_id=CHAT_ID, text=item)
        if last_msg_id:
            bot.delete_message(chat_id=CHAT_ID, message_id=last_msg_id)
        last_msg_id = msg.message_id
        time.sleep(1)

    return "Done!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
