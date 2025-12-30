from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID
from database.groups_db import groups_col

@Client.on_callback_query(filters.regex("^manage_groups$"))
async def manage_groups(client, cq):
    if cq.from_user.id != OWNER_ID:
        return await cq.answer("❌ Not authorized", show_alert=True)

    groups = list(groups_col.find({}))
    if not groups:
        return await cq.message.edit_text("❌ No groups found.\nAdd bot as admin & send /reload in group.")

    buttons = [
        [InlineKeyboardButton(g.get("group_name", str(g["_id"])), callback_data=f"open_group:{g['_id']}")]
        for g in groups
    ]

    await cq.message.edit_text(
        "📋 Select a group:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex("^open_group:"))
async def open_group_panel(client, cq):
    group_id = int(cq.data.split(":")[1])

    buttons = [
        [
            InlineKeyboardButton("✅ Turn ON", callback_data=f"welcome_on:{group_id}"),
            InlineKeyboardButton("❌ Turn OFF", callback_data=f"welcome_off:{group_id}")
        ],
        [InlineKeyboardButton("✍️ Customize message", callback_data=f"customize:{group_id}")],
        [InlineKeyboardButton("♻️ Delete last welcome", callback_data=f"delete_last:{group_id}")],
        [InlineKeyboardButton("🔙 Back", callback_data="manage_groups")]
    ]

    await cq.message.edit_text(
        f"⚙️ Welcome settings for `{group_id}`",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
