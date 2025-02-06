import asyncio
from pyrogram import Client, compose, filters, enums
import re
from pathlib import Path
from defs import getcards
from plugins.func.users_sql import *

plugins = dict(root="plugins")


async def main():
  user = Client("scrapper",
                api_id="26043952",
                api_hash="96b8dea447ef580b5b75b01ccc3ab710")
  bot = Client("@retroochk_bot",
               api_id="26043952",
               api_hash="96b8dea447ef580b5b75b01ccc3ab710",
               bot_token="7020048572:AAFoI3S5wyzXZvL2JArjsLUXvDqrPkmfUVc",
               plugins=plugins)
  clients = [user, bot]
  bot.set_parse_mode(enums.ParseMode.HTML)

  print("Done Bot Active ✅")

  await compose(clients)


