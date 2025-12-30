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

    # Add user to database
    add_user(user_id, username, first_name, last_name)

    # Buttons for user
    buttons = [
        [InlineKeyboardButton("➕ Add me to a group", url="https://t.me/YourBotUsername?startgroup=true")],
        [InlineKeyboardButton("⚙️ Manage group settings", callback_data="manage_groups")]
    ]

    # Only show "Manage group settings" button to owner/admin
    if user_id != int(OWNER_ID):
        buttons = buttons[:1]

    await message.reply(
        text=f"👋 Hello {first_name}!\nThis bot helps you manage your groups easily and safely.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
