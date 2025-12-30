from .mongo import welcome_col

def set_welcome_text(group_id: int, text: str):
    welcome_col.update_one(
        {"_id": group_id},
        {"$set": {"text": text}},
        upsert=True
    )

def get_welcome_text(group_id: int):
    doc = welcome_col.find_one({"_id": group_id})
    return doc.get("text") if doc else None

def set_welcome_media(group_id: int, media_type: str, file_id: str, caption: str = None):
    welcome_col.update_one(
        {"_id": group_id},
        {"$set": {"media": {"type": media_type, "file_id": file_id, "caption": caption}}},
        upsert=True
    )

def get_welcome_media(group_id: int):
    doc = welcome_col.find_one({"_id": group_id})
    return doc.get("media") if doc else None

def set_buttons(group_id: int, buttons: list):
    welcome_col.update_one(
        {"_id": group_id},
        {"$set": {"buttons": buttons}},
        upsert=True
    )

def get_buttons(group_id: int):
    doc = welcome_col.find_one({"_id": group_id})
    return doc.get("buttons") if doc else []
