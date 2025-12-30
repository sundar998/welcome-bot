from functools import wraps
from pyrogram import Client, filters
from config import OWNER_ID

def owner_only(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        if message.from_user.id != int(OWNER_ID):
            await message.reply("❌ You are not authorized to use this command.")
            return
        return await func(client, message, *args, **kwargs)
    return wrapper
