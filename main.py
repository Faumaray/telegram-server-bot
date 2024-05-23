import asyncio
import logging
import requests
import json

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from keep_alive import keep_alive

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7161734228:AAFb0QQ-z7HIIdXkfbVShcmIlnoKw97ZOFY")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
  r = requests.post(
      url="https://api.cloudvps.reg.ru/v1/reglets/3806197/actions",
      headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b",
          "Content-Type": "application/json"
      },
      data=json.dumps({"type": "start"}))
  logging.info(r.json())
  await message.answer(
      "Send request to start server, wait 2-5 minutes\nDont forget to stop server after session\nconnect to foundry: http://89.111.155.194:30000"
  )


@dp.message(Command("stop"))
async def stop(message: types.Message):
  r = requests.post(
      url="https://api.cloudvps.reg.ru/v1/reglets/3806197/actions",
      headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b",
          "Content-Type": "application/json"
      },
      data=json.dumps({"type": "stop"}))
  logging.info(r.json())
  await message.answer("Send request to stop server, thx for using foundry")


@dp.message(Command("status"))
async def status(message: types.Message):
  r = requests.get(
      url="https://api.cloudvps.reg.ru/v1/reglets/3806197",
      headers={
          "Authorization":
          "Bearer 168434116d655e53065dc586de58c284753c693e76c03b2f308209936783e9df9b1369eaf05999944135fa99cde4e90b"
      })
  json = r.json()
  logging.info(json)
  await message.answer("Server status: " + r.json()["reglet"]["status"])


async def main():
  keep_alive()
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())
