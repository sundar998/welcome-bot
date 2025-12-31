from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from database.welcome_db import get_welcome_text, get_welcome_media, get_buttons

@Client.on_callback_query(filters.regex("preview"))
async def preview_welcome(client: Client, cq):
    group_id = cq.from_user.id

    text = get_welcome_text(group_id) or "Welcome!"
    media = get_welcome_media(group_id)
    buttons = get_buttons(group_id)

    reply_markup = InlineKeyboardMarkup(buttons) if buttons else None

    if media:
        await client.send_cached_media(
            cq.from_user.id,
            media["file_id"],
            caption=text,
            reply_markup=reply_markup
        )
    else:
        await client.send_message(
            cq.from_user.id,
            text,
            reply_markup=reply_markup
        )
