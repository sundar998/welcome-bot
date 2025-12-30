from pyrogram import Client, filters
from pyrogram.types import Message
from database.welcome_db import set_buttons

@Client.on_message(filters.command("set_buttons") & filters.group)
async def set_buttons_handler(client: Client, message: Message):
    chat_id = message.chat.id

    if not message.reply_to_message or not message.reply_to_message.text:
        await message.reply("ℹ️ Reply to the message containing button definitions.")
        return

    text = message.reply_to_message.text
    buttons = []

    # Parse button lines
    for line in text.split("\n"):
        if " - " in line:
            parts = line.split(" - ")
            if len(parts) == 2:
                buttons.append({"text": parts[0], "url": parts[1]})
            else:
                buttons.append({"text": parts[0]})

    set_buttons(chat_id, buttons)
    await message.reply("✅ Buttons have been set successfully.")
