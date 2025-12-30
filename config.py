import os

# ---------------------------
# Telegram API
# ---------------------------
API_ID = int(os.getenv("API_ID", ""))         # Replace with your API_ID
API_HASH = os.getenv("API_HASH", "")  # Replace with your API_HASH
BOT_TOKEN = os.getenv("BOT_TOKEN", "")  # Replace with your bot token

# ---------------------------
# MongoDB
# ---------------------------
MONGO_URI = os.getenv("")

# ---------------------------
# Owner / Admin
# ---------------------------
OWNER_ID = os.getenv("")  # Telegram user ID of the bot owner

