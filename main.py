import asyncio
import logging
import requests
import json
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bearer = os.environ['BEARER']
token = os.environ['TOKEN']

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
  r = requests.post(
      url="https://api.cloudvps.reg.ru/v1/reglets/3806197/actions",
      headers={
          "Authorization":
          bearer,
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
          "Authorization": bearer,
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
          "Authorization": bearer
      })
  json = r.json()
  logging.info(json)
  await message.answer("Server status: " + r.json()["reglet"]["status"])


async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())
