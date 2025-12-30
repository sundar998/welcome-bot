from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID
from database.groups_db import groups_col

@Client.on_callback_query(filters.regex("^manage_groups$"))
async def manage_groups(client, callback_query):
    if callback_query.from_user.id != int(OWNER_ID):
        return await callback_query.answer("❌ Not authorized", show_alert=True)

    groups = list(groups_col.find({}))

    if not groups:
        return await callback_query.message.edit_text("❌ No groups found.")

    buttons = []
    for g in groups:
        buttons.append([
            InlineKeyboardButton(
                g.get("group_name", str(g["_id"])),
                callback_data=f"group_{g['_id']}"
            )
        ])

    await callback_query.message.edit_text(
        "📋 Select a group:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
