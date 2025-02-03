import asyncio
from pyrogram import Client, compose, filters, enums
import re
from pathlib import Path
from defs import getcards
from plugins.func.users_sql import *

plugins = dict(root="plugins")


async def main():
  user = Client("scrapper",
                api_id="26453853",
                api_hash="5f711fbe013fd0d20147f62728118510")
  bot = Client("my_bot",
               api_id="26453853",
               api_hash="5f711fbe013fd0d20147f62728118510"",
               bot_token="7851924299:AAEj70SJUOzeS5w-GHUpUiK-GiPV1CHRaSE",
               plugins=plugins)
  clients = [user, bot]
  bot.set_parse_mode(enums.ParseMode.HTML)

  print("Done Bot Active ✅")

  await compose(clients)


