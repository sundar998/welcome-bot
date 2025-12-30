from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.users_db import add_user
from config import OWNER_ID

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    user = message.from_user
    add_user(user.id, user.username, user.first_name, user.last_name)

    buttons = [
        [InlineKeyboardButton("➕ Add me to a group", url=f"https://t.me/{client.me.username}?startgroup=true")]
    ]

    if user.id == OWNER_ID:
        buttons.append([InlineKeyboardButton("⚙️ Manage group settings", callback_data="manage_groups")])

    await message.reply(
        "👋 Hello!\nThis bot helps you manage your groups easily and safely.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
