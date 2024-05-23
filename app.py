import telebot
import os
import time
import requests
import random
from flask import Flask
from handlers.routes import configure_routes


TOKEN = "7161734228:AAFb0QQ-z7HIIdXkfbVShcmIlnoKw97ZOFY"

bot = telebot.TeleBot(token=TOKEN, threaded=False)
app = Flask(__name__)
configure_routes(app, bot)


@bot.message_handler(commands=['start'])
def command_start(message):
    cid = message.chat.id
    r = requests.post(
        url="https://api.cloudvps.reg.ru/v1/reglets/3806197/actions",
        headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b",
          "Content-Type": "application/json"
        },
        data=json.dumps({"type": "start"}))

    bot.send_message(
        cid, "Send request to start server, wait 2-5 minutes\nDont forget to stop server after session\nconnect to foundry: http://89.111.155.194:30000")


@bot.message_handler(commands=['stop'])
def command_stop(message):
    cid = message.chat.id
    r = requests.post(
      url="https://api.cloudvps.reg.ru/v1/reglets/3806197/actions",
      headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b",
          "Content-Type": "application/json"
      },
      data=json.dumps({"type": "stop"}))

    bot.send_message(cid, "Send request to stop server, thx for using foundry")


@bot.message_handler(commands=['status'])
def command_status(message):
    cid = message.chat.id
    r = requests.get(
      url="https://api.cloudvps.reg.ru/v1/reglets/3806197",
      headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b"
      })
    json = r.json()
    logging.info(json)
    text = "Server status: " + r.json()["reglet"]["status"]
    bot.reply_to(cid, text)
