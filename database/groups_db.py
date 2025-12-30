from .mongo import groups_col

def add_group(group_id: int, group_name: str = None):
    if groups_col.find_one({"_id": group_id}):
        return False  # Group already exists
    group_data = {
        "_id": group_id,
        "group_name": group_name,
        "welcome_enabled": True,
        "media_position": "above_text",  # default
        "buttons": [],
        "last_welcome_message_id": None
    }
    groups_col.insert_one(group_data)
    return True

def get_group(group_id: int):
    return groups_col.find_one({"_id": group_id})

def update_group(group_id: int, data: dict):
    groups_col.update_one({"_id": group_id}, {"$set": data})

def total_groups():
    return groups_col.count_documents({})
