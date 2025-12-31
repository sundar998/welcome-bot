from pyrogram import Client, filters
from database.welcome_db import get_welcome_text

@Client.on_callback_query(filters.regex(r"^preview:(-?\d+)$"))
async def preview(client, cq):
    group_id = int(cq.matches[0].group(1))
    text = get_welcome_text(group_id) or "Welcome!"

    await cq.message.reply_text(f"👀 Preview:\n\n{text}")
