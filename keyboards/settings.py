from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def group_settings_keyboard(group_id: int, welcome_enabled: bool):
    status = "Active ✅" if welcome_enabled else "Inactive ❌"
    buttons = [
        [InlineKeyboardButton("❌ Turn off", callback_data=f"toggle_off_{group_id}"),
         InlineKeyboardButton("✅ Turn on", callback_data=f"toggle_on_{group_id}")],
        [InlineKeyboardButton("✍️ Customize message", callback_data=f"customize_{group_id}")],
        [InlineKeyboardButton("♻️ Delete last welcome message", callback_data=f"delete_last_{group_id}")],
        [InlineKeyboardButton("🔙 Back", callback_data="manage_groups")]
    ]
    return InlineKeyboardMarkup(buttons)
