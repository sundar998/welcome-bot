from pyrogram.types import InlineKeyboardButton

def parse_buttons(text: str):
    rows = []
    for line in text.split("\n"):
        if not line.strip():
            continue

        row = []
        buttons = line.split(" && ")
        for btn in buttons:
            title, action = btn.split(" - ", 1)

            if action.startswith("http"):
                row.append(InlineKeyboardButton(title, url=action))
            elif action.startswith("popup:") or action.startswith("alert:"):
                row.append(InlineKeyboardButton(title, callback_data=action))
            elif action == "rules":
                row.append(InlineKeyboardButton(title, callback_data="rules"))
            elif action.startswith("share:"):
                row.append(InlineKeyboardButton(title, switch_inline_query=action[6:]))
            elif action.startswith("copy:"):
                row.append(InlineKeyboardButton(title, callback_data=action))

        rows.append(row)

    return rows
