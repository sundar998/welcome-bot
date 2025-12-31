from pyrogram import Client, filters
from pyrogram.types import Message
from database.welcome_db import set_welcome_media
from utils.helpers import send_log
from config import OWNER_ID

@Client.on_message(filters.private & (filters.photo | filters.video | filters.animation | filters.sticker))
async def set_media(client: Client, message: Message):
    if message.from_user.id != int(OWNER_ID):
        return

    group_id = message.chat.id

    file_id = (
        message.photo.file_id if message.photo else
        message.video.file_id if message.video else
        message.animation.file_id if message.animation else
        message.sticker.file_id
    )

    caption = message.caption or None

    set_welcome_media(group_id, file_id, caption)

    await message.reply("✅ Media saved successfully")
    await send_log(client, f"📷 Media updated for group {group_id}")
