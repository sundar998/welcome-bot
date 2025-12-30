from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.groups_db import get_group

@Client.on_callback_query(filters.regex("manage_groups"))
async def manage_groups(client: Client, callback_query):
    user_id = callback_query.from_user.id
    # Only OWNER can manage groups
    from config import OWNER_ID
    if user_id != int(OWNER_ID):
        await callback_query.answer("❌ You are not authorized.", show_alert=True)
        return

    # List all groups
    from database.groups_db import groups_col
    groups = groups_col.find({})
    buttons = []
    for g in groups:
        buttons.append([InlineKeyboardButton(g.get("group_name", str(g["_id"])), callback_data=f"group_{g['_id']}")])

    await callback_query.message.edit_text(
        "📋 Select a group to manage:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
