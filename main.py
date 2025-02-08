import asyncio
import os
from pyrogram import Client, enums
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("Faltan credenciales en las variables de entorno")

plugins = dict(root="plugins")

async def main():
    """Función principal para ejecutar el bot."""
    try:
        bot = Client("retroochk_bot",
                     api_id=API_ID,
                     api_hash=API_HASH,
                     bot_token=BOT_TOKEN,
                     plugins=plugins)

        bot.set_parse_mode(enums.ParseMode.HTML)
        print("✅ Bot Activo")

        await bot.start()
        await asyncio.Event().wait()  # Mantener el bot en ejecución

    except Exception as e:
        print(f"❌ Error al iniciar el bot: {e}")

if __name__ == "__main__":
    asyncio.run(main())
