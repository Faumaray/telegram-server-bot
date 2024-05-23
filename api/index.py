import os
from flask import Flask, Response

import requests
import json
from teleflask import Teleflask
from teleflask.messages import TextMessage

app = Flask(__name__)

API_KEY = "7161734228:AAFb0QQ-z7HIIdXkfbVShcmIlnoKw97ZOFY"
bot = Teleflask(API_KEY, app)

@app.route("/api")
def index():
    return "This is awesome, isn't it?"
# end def


# Register the /start command
@bot.command("start")
def start(update, text):
    r = requests.post(
        url="https://api.cloudvps.reg.ru/v1/reglets/3806197/actions",
        headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b",
          "Content-Type": "application/json"
        },
        data=json.dumps({"type": "start"}))

    # update is the update object. It is of type pytgbot.api_types.receivable.updates.Update
    # text is the text after the command. Can be empty. Type is str.
    return TextMessage("Send request to start server, wait 2-5 minutes\nDont forget to stop server after session\nconnect to foundry: http://89.111.155.194:30000", parse_mode="html")
# end def
@bot.command("stop")
def stop(update, text):
    r = requests.post(
      url="https://api.cloudvps.reg.ru/v1/reglets/3806197/actions",
      headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b",
          "Content-Type": "application/json"
      },
      data=json.dumps({"type": "stop"}))
    logging.info(r.json())
    return TextMessage("Send request to stop server, thx for using foundry", parse_mode="html")

@bot.command("status")
def status(update, text):
    r = requests.get(
      url="https://api.cloudvps.reg.ru/v1/reglets/3806197",
      headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b"
      })
    json = r.json()
    logging.info(json)
    text = "Server status: " + r.json()["reglet"]["status"]
    return TextMessage(text, parse_mode="html")

# register a function to be called for updates.
@bot.on_update
def foo(update):
    from pytgbot.api_types.receivable.updates import Update
    assert isinstance(update, Update)
    # do stuff with the update
    # you can use bot.bot to access the pytgbot.Bot's messages functions
    if not update.message:
        return
        # you could use @bot.on_message instead of this if.
    # end if
    # end def
