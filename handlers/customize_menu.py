from pyrogram import Client, filters
from keyboards.customize import customize_menu

@Client.on_callback_query(filters.regex(r"^customize:(-?\d+)$"))
async def open_customize_menu(client, cq):
    group_id = int(cq.matches[0].group(1))

    await cq.message.edit_text(
        "🎨 Customize Welcome Message",
        reply_markup=customize_menu(group_id)
    )
