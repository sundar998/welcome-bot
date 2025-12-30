from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.groups_db import get_group, update_group
from database.welcome_db import get_welcome_text, get_welcome_media, get_buttons
from utils.helpers import send_log       # <-- Added
from config import LOG_CHANNEL           # <-- Added

@Client.on_message(filters.new_chat_members)
async def welcome_new_member(client: Client, message: Message):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if not group or not group.get("welcome_enabled", True):
        return

    # Delete last welcome message if exists
    last_msg_id = group.get("last_welcome_message_id")
    if last_msg_id:
        try:
            await client.delete_messages(chat_id, last_msg_id)
        except:
            pass

    # Prepare welcome message
    text = get_welcome_text(chat_id) or "Welcome {MENTION}!"
    for user in message.new_chat_members:
        formatted_text = text.replace("{NAME}", user.first_name or "") \
                             .replace("{SURNAME}", user.last_name or "") \
                             .replace("{NAMESURNAME}", f"{user.first_name or ''} {user.last_name or ''}") \
                             .replace("{ID}", str(user.id)) \
                             .replace("{USERNAME}", f"@{user.username}" if user.username else "") \
                             .replace("{MENTION}", f"[{user.first_name}](tg://user?id={user.id})") \
                             .replace("{GROUPNAME}", message.chat.title or "")

        media = get_welcome_media(chat_id)
        buttons_data = get_buttons(chat_id)
        buttons = []
        for row in buttons_data:
            buttons.append([InlineKeyboardButton(text=b["text"], url=b.get("url"))])

        reply_markup = InlineKeyboardMarkup(buttons) if buttons else None

        # Send message
        if media:
            msg = await client.send_cached_media(
                chat_id,
                file_id=media["file_id"],
                caption=formatted_text if media.get("caption") else None,
                reply_markup=reply_markup
            )
        else:
            msg = await client.send_message(chat_id, formatted_text, reply_markup=reply_markup)

        # Save last welcome message ID
        update_group(chat_id, {"last_welcome_message_id": msg.message_id})

        # -------------------------
        # Send log to log channel
        # -------------------------
        if LOG_CHANNEL:
            await send_log(client, f"👋 Welcome message sent to {user.first_name} ({user.id}) in {message.chat.title} ({chat_id})")
