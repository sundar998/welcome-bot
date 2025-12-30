from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_panel_keyboard():
    buttons = [
        [InlineKeyboardButton("📋 List Groups", callback_data="groups_list")],
        [InlineKeyboardButton("📊 Stats Users", callback_data="stats_users"),
         InlineKeyboardButton("📊 Stats Groups", callback_data="stats_groups")],
        [InlineKeyboardButton("🔙 Back", callback_data="start")]
    ]
    return InlineKeyboardMarkup(buttons)
