import asyncio
import os
from pyrogram import Client, compose, enums
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Obtener credenciales de forma segura
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Verificar que las credenciales existen
if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("Faltan credenciales en las variables de entorno")

# Configurar plugins
plugins = dict(root="plugins")

async def main():
    """Función principal para ejecutar los clientes de Pyrogram."""
    try:
        user = Client("scrapper", api_id=API_ID, api_hash=API_HASH)
        bot = Client("my_bot",
                     api_id=API_ID,
                     api_hash=API_HASH,
                     bot_token=BOT_TOKEN,
                     plugins=plugins)

        # Configurar el parseo de mensajes en HTML
        bot.set_parse_mode(enums.ParseMode.HTML)

        print("✅ Bot Activo")

        # Ejecutar los clientes simultáneamente
        await compose([user, bot])

    except Exception as e:
        print(f"❌ Error al iniciar el bot: {e}")

if __name__ == "__main__":
    asyncio.run(main())
