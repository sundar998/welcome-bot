from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def customize_menu(group_id: int):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📄 Text", callback_data=f"set_text:{group_id}")],
            [InlineKeyboardButton("📷 Media", callback_data=f"set_media:{group_id}")],
            [InlineKeyboardButton("🔗 URL Buttons", callback_data=f"set_buttons:{group_id}")],
            [InlineKeyboardButton("👀 Preview", callback_data=f"preview:{group_id}")],
            [InlineKeyboardButton("🔙 Back", callback_data="manage_groups")]
        ]
    )
