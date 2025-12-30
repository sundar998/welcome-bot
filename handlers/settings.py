from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID
from database.groups_db import groups_col

@Client.on_callback_query(filters.regex("^manage_groups$"))
async def manage_groups(client: Client, callback_query):
    if callback_query.from_user.id != int(OWNER_ID):
        await callback_query.answer("❌ You are not authorized", show_alert=True)
        return

    groups = list(groups_col.find({}))

    if not groups:
        await callback_query.message.edit_text(
            "⚠️ No groups found.\n\n"
            "➕ Add the bot to a group as ADMIN\n"
            "Then send /reload in that group."
        )
        return

    buttons = []
    for g in groups:
        buttons.append([
            InlineKeyboardButton(
                text=g.get("group_name", str(g["_id"])),
                callback_data=f"group_{g['_id']}"
            )
        ])

    await callback_query.message.edit_text(
        "📋 Select a group to manage:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
