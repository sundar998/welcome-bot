from pyrogram import Client, filters
from database.welcome_db import set_text

@Client.on_message(filters.group & filters.command("setwelcome"))
async def set_welcome(client, message):
    admins = [m.user.id for m in await client.get_chat_members(
        message.chat.id,
        filter="administrators"
    )]

    if message.from_user.id not in admins:
        return await message.reply("❌ Admin only")

    args = message.text.split(None, 1)
    if len(args) < 2:
        return await message.reply("Usage:\n/setwelcome Welcome text")

    set_text(message.chat.id, args[1])
    await message.reply("✅ Welcome message updated")
