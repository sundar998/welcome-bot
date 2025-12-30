from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.groups_db import get_group
from database.welcome_db import get_welcome_text, get_welcome_media, get_buttons

@Client.on_callback_query(filters.regex("preview"))
async def preview_welcome(client: Client, callback_query):
    chat_id = int(callback_query.data.split("_")[1])
    group = get_group(chat_id)
    if not group:
        await callback_query.answer("❌ Group not found.", show_alert=True)
        return

    text = get_welcome_text(chat_id) or "Welcome!"
    media = get_welcome_media(chat_id)
    buttons_data = get_buttons(chat_id)

    buttons = []
    for row in buttons_data:
        buttons.append([InlineKeyboardButton(text=b["text"], url=b.get("url"))])
    reply_markup = InlineKeyboardMarkup(buttons) if buttons else None

    if media:
        await client.send_cached_media(
            chat_id,
            file_id=media["file_id"],
            caption=text if media.get("caption") else None,
            reply_markup=reply_markup
        )
    else:
        await client.send_message(chat_id, text, reply_markup=reply_markup)
