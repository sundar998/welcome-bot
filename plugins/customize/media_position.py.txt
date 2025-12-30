from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.welcome_db import set_media_position

@Client.on_callback_query(filters.regex(r"media_position_(above|below)_\d+"))
async def toggle_media_position(client: Client, callback_query):
    action, chat_id = callback_query.data.split("_")[2], int(callback_query.data.split("_")[3])
    position = "above" if action == "above" else "below"

    set_media_position(chat_id, position)
    await callback_query.answer(f"✅ Media position set to {position}.", show_alert=True)
