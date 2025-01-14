from flask import Flask
from threading import Thread
from waitress import serve

app = Flask('')


@app.route('/')
def home():
    return "Bot is online!"


def run():
    serve(app, host="0.0.0.0", port=8080)  # production server using waitress
    # app.run(host='0.0.0.0',port=8080) #development server


def start_server():
    t = Thread(target=run)
    t.start()
