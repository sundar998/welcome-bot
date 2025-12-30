from datetime import datetime

def format_username(user):
    if user.username:
        return f"@{user.username}"
    return f"{user.first_name} {user.last_name or ''}".strip()

def current_time():
    return datetime.now().strftime("%H:%M:%S")

def current_date():
    return datetime.now().strftime("%d-%m-%Y")

def weekday():
    return datetime.now().strftime("%A")
