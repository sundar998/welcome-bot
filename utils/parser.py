import re

def parse_placeholders(text: str, user, group_name: str):
    """
    Replace placeholders in welcome text with actual values.
    Supported placeholders:
    {ID}, {NAME}, {SURNAME}, {NAMESURNAME}, {USERNAME}, {MENTION}, {LANG}, {DATE}, {TIME}, {WEEKDAY}, {GROUPNAME}
    """
    replacements = {
        "{ID}": str(user.id),
        "{NAME}": user.first_name,
        "{SURNAME}": user.last_name or "",
        "{NAMESURNAME}": f"{user.first_name} {user.last_name or ''}".strip(),
        "{USERNAME}": f"@{user.username}" if user.username else user.first_name,
        "{MENTION}": f"[{user.first_name}](tg://user?id={user.id})",
        "{LANG}": getattr(user, "language_code", "en"),
        "{DATE}": __import__("datetime").datetime.now().strftime("%d-%m-%Y"),
        "{TIME}": __import__("datetime").datetime.now().strftime("%H:%M:%S"),
        "{WEEKDAY}": __import__("datetime").datetime.now().strftime("%A"),
        "{GROUPNAME}": group_name
    }

    for key, value in replacements.items():
        text = text.replace(key, value)
    return text
