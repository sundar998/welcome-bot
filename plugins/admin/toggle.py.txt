from pyrogram import Client, filters
from database.groups_db import update_group

@Client.on_callback_query(filters.regex(r"toggle_(on|off)_\d+"))
async def toggle_welcome(client: Client, callback_query):
    action, group_id = callback_query.data.split("_")[1], int(callback_query.data.split("_")[2])
    status = True if action == "on" else False

    update_group(group_id, {"welcome_enabled": status})

    await callback_query.answer(f"✅ Welcome message {'enabled' if status else 'disabled'} for this group.")
    await callback_query.message.edit_text("Status updated. Use the panel to see changes.")
