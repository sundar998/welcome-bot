from pyrogram import Client, filters
from database.groups_db import get_group, update_group
from pyrogram.errors import MessageIdInvalid

@Client.on_callback_query(filters.regex(r"delete_last_\d+"))
async def delete_last_welcome(client: Client, callback_query):
    group_id = int(callback_query.data.split("_")[2])
    group = get_group(group_id)
    if not group:
        await callback_query.answer("❌ Group not found.", show_alert=True)
        return

    last_msg_id = group.get("last_welcome_message_id")
    if last_msg_id:
        try:
            await client.delete_messages(group_id, last_msg_id)
            update_group(group_id, {"last_welcome_message_id": None})
            await callback_query.answer("♻️ Last welcome message deleted.", show_alert=True)
        except MessageIdInvalid:
            await callback_query.answer("❌ No message found to delete.", show_alert=True)
    else:
        await callback_query.answer("ℹ️ No previous welcome message to delete.", show_alert=True)
