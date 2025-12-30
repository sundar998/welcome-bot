from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.groups_db import groups_col

@Client.on_callback_query(filters.regex("groups_list"))
async def list_groups(client: Client, callback_query):
    groups = groups_col.find({})
    buttons = []

    for g in groups:
        buttons.append([InlineKeyboardButton(g.get("group_name", str(g["_id"])), callback_data=f"group_{g['_id']}")])

    await callback_query.message.edit_text(
        "📋 List of groups:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
