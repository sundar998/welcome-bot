import os

# ---------------------------
# Telegram API
# ---------------------------
API_ID = int(os.getenv("API_ID", "123456"))         # Replace with your API_ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with your API_HASH
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Replace with your bot token

# ---------------------------
# MongoDB
# ---------------------------
MONGO_URI = os.getenv("MONGO_URI")

# ---------------------------
# Owner / Admin
# ---------------------------
OWNER_ID = os.getenv("OWNER_ID")  # Telegram user ID of the bot owner
