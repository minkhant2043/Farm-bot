from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio
import logging
import os

# Enable logging
logging.basicConfig(level=logging.INFO)

# Replace with your actual bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    BOT_TOKEN = "7589349942:AAH8STVqov09vLQ3hR6fLfAJ44IatalrbiI"

# Replace with your actual game bot username (e.g. @example_farmbot)
GAME_BOT_USERNAME =  "@AutofarmMinKhant_bot"

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# When the bot receives "/start", it will reply
@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.reply("🤖 Auto farming bot has started!\nPlease wait...")

    # Start the auto farming task
    asyncio.create_task(start_auto_farming(message.chat.id))

# Farming loop (repeat sending command every 20 seconds)
async def start_auto_farming(chat_id):
    while True:
        try:
            await bot.send_message(chat_id=chat_id, text=f"{GAME_BOT_USERNAME}")
            await asyncio.sleep(1.5)
            await bot.send_message(chat_id=chat_id, text="/farm")  # Send farming command
            await asyncio.sleep(20)  # Wait before next farm
        except Exception as e:
            logging.error(f"Error occurred: {e}")
            await asyncio.sleep(10)  # Retry delay

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
