from pyrogram import Client, filters
from database.groups_db import groups_col
from config import OWNER_ID

@Client.on_message(filters.command("stats_groups") & filters.private)
async def stats_groups(client: Client, message):
    user_id = message.from_user.id
    if user_id != int(OWNER_ID):
        await message.reply("❌ You are not authorized.")
        return

    total = groups_col.count_documents({})
    await message.reply(f"📊 Total groups in the database: {total}")
