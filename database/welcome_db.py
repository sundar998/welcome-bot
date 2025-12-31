from database.mongo import welcome_col

def set_welcome_media(group_id, file_id, caption=None):
    welcome_col.update_one(
        {"_id": group_id},
        {"$set": {"media": {"file_id": file_id, "caption": caption}}},
        upsert=True
    )

def get_welcome_media(group_id):
    data = welcome_col.find_one({"_id": group_id})
    return data.get("media") if data else None

def set_buttons(group_id, buttons):
    welcome_col.update_one(
        {"_id": group_id},
        {"$set": {"buttons": buttons}},
        upsert=True
    )

def get_buttons(group_id):
    data = welcome_col.find_one({"_id": group_id})
    return data.get("buttons", []) if data else []

def get_welcome_text(group_id):
    data = welcome_col.find_one({"_id": group_id})
    return data.get("text") if data else None
