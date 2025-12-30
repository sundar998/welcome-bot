from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.users_db import add_user
from config import OWNER_ID

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    add_user(user_id, username, first_name, last_name)

    buttons = [
        [InlineKeyboardButton("➕ Add me to a group", url="https://t.me/Demodemo1617_robot?startgroup=true")]
    ]

    # Show manage button ONLY if OWNER_ID exists and matches
    if OWNER_ID and user_id == OWNER_ID:
        buttons.append(
            [InlineKeyboardButton("⚙️ Manage group settings", callback_data="manage_groups")]
        )

    await message.reply(
        text=f"👋 Hello {first_name}!\nThis bot helps you manage your groups easily and safely.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
