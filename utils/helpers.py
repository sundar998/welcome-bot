from datetime import datetime
from config import LOG_CHANNEL

# -------------------------
# User formatting helpers
# -------------------------
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

# -------------------------
# Log channel helper
# -------------------------
async def send_log(client, text):
    if not LOG_CHANNEL:
        return
    try:
        await client.send_message(LOG_CHANNEL, text)
    except Exception as e:
        print(f"❌ Log send failed: {e}")
