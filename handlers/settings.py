from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.groups_db import get_group, groups_col
from config import OWNER_ID, LOG_CHANNEL

# -------------------------
# Manage groups panel
# -------------------------
@Client.on_callback_query(filters.regex("manage_groups"))
async def manage_groups(client: Client, callback_query):
    user_id = callback_query.from_user.id

    if user_id != int(OWNER_ID):
        await callback_query.answer("❌ You are not authorized.", show_alert=True)
        return

    groups = groups_col.find({})
    buttons = []

    for g in groups:
        buttons.append([
            InlineKeyboardButton(
                g.get("group_name", str(g["_id"])),
                callback_data=f"group_{g['_id']}"
            )
        ])

    await callback_query.message.edit_text(
        "📋 Select a group to manage:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    # -------- LOG --------
    if LOG_CHANNEL:
        await client.send_message(
            LOG_CHANNEL,
            f"⚙️ MANAGE GROUPS OPENED\n"
            f"👤 Admin: {callback_query.from_user.first_name} ({user_id})"
        )
