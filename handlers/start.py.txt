from pyrogram import Client, filters
from keyboards.start import start_keyboard

@Client.on_message(filters.private & filters.command("start"))
async def start_handler(client, message):
    await message.reply(
        "👋 Hello!\n\nThis bot helps you manage your groups easily and safely.",
        reply_markup=start_keyboard()
    )
