from pyrogram import Client
from pyrogram.types import Message
from database.welcome_db import get_settings
from utils.formatter import format_text

@Client.on_message()
async def welcome_user(client, message: Message):
    if not message.new_chat_members:
        return

    settings = get_settings(message.chat.id)
    if not settings["enabled"]:
        return

    for user in message.new_chat_members:
        text = format_text(settings["text"], user, message.chat)
        await message.reply(text, disable_web_page_preview=True)
