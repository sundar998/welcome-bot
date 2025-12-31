from pyrogram import Client, filters
from database.welcome_db import set_welcome_text

@Client.on_callback_query(filters.regex(r"^set_text:(-?\d+)$"))
async def text_setup(client, cq):
    group_id = int(cq.matches[0].group(1))

    await cq.message.reply_text(
        "Send now the message you want to set!\n\n"
        "{NAME} {SURNAME} {USERNAME} {MENTION} {GROUPNAME}"
    )

    client.user_data = {"text_group": group_id}

@Client.on_message(filters.text & filters.private)
async def save_text(client, message):
    if not hasattr(client, "user_data"):
        return
    if "text_group" not in client.user_data:
        return

    group_id = client.user_data.pop("text_group")
    set_welcome_text(group_id, message.text)

    await message.reply("✅ Welcome text saved")
