from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def customize_menu_keyboard(group_id: int):
    buttons = [
        [InlineKeyboardButton("📄 Text", callback_data=f"custom_text_{group_id}")],
        [InlineKeyboardButton("📷 Media", callback_data=f"custom_media_{group_id}")],
        [InlineKeyboardButton("🔗 URL Buttons", callback_data=f"custom_buttons_{group_id}")],
        [InlineKeyboardButton("🖼️ Media below text", callback_data=f"media_position_toggle_{group_id}")],
        [InlineKeyboardButton("👀 Full preview", callback_data=f"preview_customize_{group_id}")],
        [InlineKeyboardButton("🔙 Back", callback_data=f"group_{group_id}")]
    ]
    return InlineKeyboardMarkup(buttons)
