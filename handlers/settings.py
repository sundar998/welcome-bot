from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.groups_db import get_group
from config import OWNER_ID

# --------------------
# SHOW GROUP LIST
# --------------------
@Client.on_callback_query(filters.regex("^manage_groups$"))
async def manage_groups(client, cq):
    if cq.from_user.id != OWNER_ID:
        return await cq.answer("Not allowed", show_alert=True)

    from database.groups_db import groups_col
    buttons = []

    for g in groups_col.find({}):
        buttons.append([
            InlineKeyboardButton(
                g.get("group_name", str(g["_id"])),
                callback_data=f"group:{g['_id']}"
            )
        ])

    if not buttons:
        return await cq.message.edit_text("❌ No groups found")

    await cq.message.edit_text(
        "📋 Select a group:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


# --------------------
# GROUP SETTINGS PANEL
# --------------------
@Client.on_callback_query(filters.regex("^group:"))
async def group_settings(client, cq):
    if cq.from_user.id != OWNER_ID:
        return

    group_id = int(cq.data.split(":")[1])
    group = get_group(group_id)

    if not group:
        return await cq.answer("Group not found", show_alert=True)

    status = "✅ ON" if group.get("welcome_enabled", True) else "❌ OFF"

    buttons = [
        [
            InlineKeyboardButton("✅ Turn ON", callback_data=f"welcome:on:{group_id}"),
            InlineKeyboardButton("❌ Turn OFF", callback_data=f"welcome:off:{group_id}")
        ],
        [
            InlineKeyboardButton("✍️ Customize Message", callback_data=f"customize:{group_id}")
        ],
        [
            InlineKeyboardButton("♻️ Delete Last Welcome", callback_data=f"delete:{group_id}")
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="manage_groups")
        ]
    ]

    await cq.message.edit_text(
        f"⚙️ Group Settings\n\nStatus: {status}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
