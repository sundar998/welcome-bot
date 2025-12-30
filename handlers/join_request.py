from pyrogram import Client
from pyrogram.types import ChatJoinRequest

@Client.on_chat_join_request()
async def auto_approve(client, req: ChatJoinRequest):
    await req.approve()
