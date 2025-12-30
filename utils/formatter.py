from datetime import datetime

def format_text(text, user, chat):
    return text.format(
        ID=user.id,
        NAME=user.first_name or "",
        SURNAME=user.last_name or "",
        USERNAME=user.username or "",
        GROUPNAME=chat.title or "",
        DATE=datetime.now().strftime("%d-%m-%Y"),
        TIME=datetime.now().strftime("%H:%M"),
        MENTION=f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
    )
