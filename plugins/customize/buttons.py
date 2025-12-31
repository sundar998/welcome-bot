from pyrogram import Client, filters
from database.welcome_db import set_buttons

@Client.on_callback_query(filters.regex(r"^set_buttons:(-?\d+)$"))
async def buttons_setup(client, cq):
    group_id = int(cq.matches[0].group(1))
    client.user_data = {"btn_group": group_id}

    await cq.message.reply_text(
        "Send buttons like:\n\n"
        "Google - https://google.com\n"
        "Telegram - https://t.me"
    )

@Client.on_message(filters.text & filters.private)
async def save_buttons(client, message):
    if not hasattr(client, "user_data"):
        return
    if "btn_group" not in client.user_data:
        return

    group_id = client.user_data.pop("btn_group")
    rows = []

    for line in message.text.splitlines():
        if "-" in line:
            t, u = line.split("-", 1)
            rows.append([[t.strip(), u.strip()]])

    set_buttons(group_id, rows)
    await message.reply("✅ Buttons saved")
