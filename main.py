import asyncio
import os
from pyrogram import Client, compose, enums
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener credenciales de forma segura
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

plugins = dict(root="plugins")

async def main():
    user = Client("scrapper", api_id=API_ID, api_hash=API_HASH)
    bot = Client("my_bot",
                 api_id=API_ID,
                 api_hash=API_HASH,
                 bot_token=BOT_TOKEN,
                 plugins=plugins)
    
    bot.set_parse_mode(enums.ParseMode.HTML)
    
    print("✅ Bot Activo")
    
    # Ejecutar múltiples clientes
    await compose([user, bot])

if __name__ == "__main__":
    asyncio.run(main())
