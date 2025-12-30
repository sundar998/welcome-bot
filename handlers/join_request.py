from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from database.groups_db import get_group
from database.stats_db import increment_user_joins
from utils.helpers import send_log  # <-- Added
from config import LOG_CHANNEL      # <-- Added

@Client.on_chat_join_request()
async def auto_approve(client: Client, join_request: ChatJoinRequest):
    group_id = join_request.chat.id
    user_id = join_request.from_user.id

    # Check if group exists and welcome is enabled
    group = get_group(group_id)
    if group is None:
        return  # Group not configured

    # Auto approve join request
    try:
        await client.approve_chat_join_request(group_id, user_id)
    except Exception as e:
        print(f"❌ Failed to approve join request: {e}")
        return

    # Increment stats
    increment_user_joins(group_id)

    # -------------------------
    # Send log to log channel
    # -------------------------
    if LOG_CHANNEL:
        user_name = join_request.from_user.first_name
        user_username = join_request.from_user.username or "NoUsername"
        chat_title = join_request.chat.title
        await send_log(client, f"👤 New user joined: {user_name} (@{user_username}) in {chat_title} ({group_id})")
