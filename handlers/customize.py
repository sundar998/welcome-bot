from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID

@Client.on_callback_query(filters.regex("^customize:"))
async def customize_menu(client, cq):
    if cq.from_user.id != OWNER_ID:
        return

    group_id = int(cq.data.split(":")[1])

    buttons = [
        [InlineKeyboardButton("📄 Text", callback_data=f"text:{group_id}")],
        [InlineKeyboardButton("📷 Media", callback_data=f"media:{group_id}")],
        [InlineKeyboardButton("🔗 URL Buttons", callback_data=f"buttons:{group_id}")],
        [InlineKeyboardButton("👀 Preview", callback_data=f"preview:{group_id}")],
        [InlineKeyboardButton("🔙 Back", callback_data=f"group:{group_id}")]
    ]

    await cq.message.edit_text(
        "✍️ Customize Welcome Message",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
