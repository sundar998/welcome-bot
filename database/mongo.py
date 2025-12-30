from pymongo import MongoClient
import os

# ---------------------------
# MongoDB Connection
# ---------------------------

# Get MongoDB URI from environment variable
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI is not set in environment variables!")

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Database name
db = client["welcome_bot_db"]

# ---------------------------
# Collections
# ---------------------------
users_col = db["users"]          # Store users who started bot
groups_col = db["groups"]        # Store group-wise settings
welcome_col = db["welcome"]      # Store welcome messages & media per group
stats_col = db["stats"]          # Store statistics: user joins, messages, etc.

print("✅ MongoDB connected successfully")
