from pyrogram import Client, filters
from pyrogram.types import Message
from database.welcome_db import set_welcome_media

@Client.on_message(filters.command("set_media") & filters.group)
async def set_welcome_media_handler(client: Client, message: Message):
    chat_id = message.chat.id

    if not message.reply_to_message:
        await message.reply("ℹ️ Reply to the media message you want to set as welcome.")
        return

    reply = message.reply_to_message

    media_type = None
    file_id = None
    caption = reply.caption if reply.caption else None

    if reply.photo:
        media_type = "photo"
        file_id = reply.photo.file_id
    elif reply.video:
        media_type = "video"
        file_id = reply.video.file_id
    elif reply.animation:
        media_type = "animation"
        file_id = reply.animation.file_id
    elif reply.sticker:
        media_type = "sticker"
        file_id = reply.sticker.file_id

    if not file_id:
        await message.reply("❌ No valid media found in the replied message.")
        return

    set_welcome_media(chat_id, media_type, file_id, caption)
    await message.reply(f"✅ Welcome {media_type} has been set successfully.")
