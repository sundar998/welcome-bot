from database.mongo import db

col = db["WELCOME_SETTINGS"]

def get_settings(chat_id):
    data = col.find_one({"chat_id": chat_id})
    if not data:
        data = {
            "chat_id": chat_id,
            "enabled": True,
            "text": "👋 Welcome {MENTION} to {GROUPNAME}!"
        }
        col.insert_one(data)
    return data

def set_text(chat_id, text):
    col.update_one(
        {"chat_id": chat_id},
        {"$set": {"text": text}},
        upsert=True
    )
