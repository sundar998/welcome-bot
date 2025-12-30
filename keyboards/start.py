from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():
    return InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                "➕ Add me to a group",
                url="https://t.me/Demodemo1617_robot?startgroup=true"
            )
        ]]
    )

