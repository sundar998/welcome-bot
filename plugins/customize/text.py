from pyrogram import Client, filters
from database.welcome_db import set_welcome_text
from pyrogram.types import Message

@Client.on_message(filters.command("set_text") & filters.group)
async def set_welcome_text_handler(client: Client, message: Message):
    chat_id = message.chat.id

    if not message.reply_to_message or not message.reply_to_message.text:
        await message.reply("ℹ️ Reply to the message containing the welcome text you want to set.")
        return

    text = message.reply_to_message.text
    set_welcome_text(chat_id, text)
    await message.reply("✅ Welcome text has been set successfully.")
