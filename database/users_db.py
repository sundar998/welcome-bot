from .mongo import users_col
from datetime import datetime

def add_user(user_id: int, username: str = None, first_name: str = None, last_name: str = None):
    if users_col.find_one({"_id": user_id}):
        return False  # User already exists
    user_data = {
        "_id": user_id,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "joined_at": datetime.utcnow()
    }
    users_col.insert_one(user_data)
    return True

def get_user(user_id: int):
    return users_col.find_one({"_id": user_id})

def total_users():
    return users_col.count_documents({})
