from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():
    buttons = [
        [InlineKeyboardButton("➕ Add me to a group", url="https://t.me/Demodemo1617_robot?startgroup=true")],
        [InlineKeyboardButton("⚙️ Manage group settings", callback_data="manage_groups")]
    ]
    return InlineKeyboardMarkup(buttons)
