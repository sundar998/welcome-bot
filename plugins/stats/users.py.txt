from pyrogram import Client, filters
from database.users_db import users_col
from config import OWNER_ID

@Client.on_message(filters.command("stats_users") & filters.private)
async def stats_users(client: Client, message):
    user_id = message.from_user.id
    if user_id != int(OWNER_ID):
        await message.reply("❌ You are not authorized.")
        return

    total = users_col.count_documents({})
    await message.reply(f"📊 Total users in the database: {total}")
