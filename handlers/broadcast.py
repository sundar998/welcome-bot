from pyrogram import Client, filters
from database.users_db import total_users, users_col
from config import OWNER_ID

@Client.on_message(filters.command("broadcast") & filters.private)
async def broadcast_message(client: Client, message):
    user_id = message.from_user.id
    if user_id != int(OWNER_ID):
        await message.reply("❌ You are not authorized to broadcast messages.")
        return

    if not message.reply_to_message:
        await message.reply("ℹ️ Reply to the message you want to broadcast with /broadcast.")
        return

    broadcast_msg = message.reply_to_message

    users = users_col.find({})
    success = 0
    failed = 0

    for user in users:
        try:
            await broadcast_msg.copy(user["_id"])
            success += 1
        except:
            failed += 1

    await message.reply(f"✅ Broadcast completed!\n\nSuccess: {success}\nFailed: {failed}")
