from pyrogram import Client, filters
from pyrogram.types import Message
from keyboards.buttons_parser import parse_buttons
from database.welcome_db import set_buttons
from utils.helpers import send_log
from config import OWNER_ID

@Client.on_message(filters.private & filters.text)
async def set_buttons_handler(client: Client, message: Message):
    if message.from_user.id != int(OWNER_ID):
        return

    buttons = parse_buttons(message.text)
    set_buttons(message.chat.id, buttons)

    await message.reply("✅ Buttons saved successfully")
    await send_log(client, f"🔗 Buttons updated for group {message.chat.id}")
