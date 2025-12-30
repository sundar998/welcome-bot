from pyrogram import Client, filters
from database.groups_db import add_group

@Client.on_message(filters.command("reload") & filters.group)
async def reload_group(client: Client, message):
    group_id = message.chat.id
    group_name = message.chat.title

    if add_group(group_id, group_name):
        await message.reply(f"✅ Group `{group_name}` has been added to the database.")
    else:
        await message.reply(f"ℹ️ Group `{group_name}` already exists in the database.")
