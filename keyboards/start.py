from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():
    return InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "➕ Add me to a group",
                url="https://t.me/your_bot_username?startgroup=true"
            )
        ]]
    )
