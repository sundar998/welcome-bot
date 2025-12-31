from pyrogram import Client, filters
from database.welcome_db import set_welcome_media

@Client.on_callback_query(filters.regex(r"^set_media:(-?\d+)$"))
async def media_setup(client, cq):
    group_id = int(cq.matches[0].group(1))
    client.user_data = {"media_group": group_id}

    await cq.message.reply_text("👉 Send photo / video / gif")

@Client.on_message(filters.media & filters.private)
async def save_media(client, message):
    if not hasattr(client, "user_data"):
        return
    if "media_group" not in client.user_data:
        return

    group_id = client.user_data.pop("media_group")

    file_id = (
        message.photo.file_id if message.photo else
        message.video.file_id if message.video else
        message.animation.file_id
    )

    set_welcome_media(group_id, file_id)
    await message.reply("✅ Media saved")
