import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = int(os.getenv("8054916377"))   # REQUIRED
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL")) if os.getenv("LOG_CHANNEL") else None

