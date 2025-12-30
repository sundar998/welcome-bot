from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.groups_db import get_group, update_group

@Client.on_callback_query(filters.regex(r"group_\d+"))
async def group_panel(client: Client, callback_query):
    group_id = int(callback_query.data.split("_")[1])
    group = get_group(group_id)
    if not group:
        await callback_query.answer("❌ Group not found.", show_alert=True)
        return

    status = "Active ✅" if group.get("welcome_enabled", True) else "Inactive ❌"

    buttons = [
        [InlineKeyboardButton("❌ Turn off", callback_data=f"toggle_off_{group_id}"),
         InlineKeyboardButton("✅ Turn on", callback_data=f"toggle_on_{group_id}")],
        [InlineKeyboardButton("✍️ Customize message", callback_data=f"customize_{group_id}")],
        [InlineKeyboardButton("♻️ Delete last welcome message", callback_data=f"delete_last_{group_id}")],
        [InlineKeyboardButton("🔙 Back", callback_data="manage_groups")]
    ]

    await callback_query.message.edit_text(
        f"📌 Group: {group.get('group_name', group_id)}\nStatus: {status}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
