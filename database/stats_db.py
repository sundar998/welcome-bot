from .mongo import stats_col
from datetime import datetime

def increment_user_joins(group_id: int):
    stats_col.update_one(
        {"_id": group_id},
        {"$inc": {"user_joins": 1}},
        upsert=True
    )

def increment_messages(group_id: int):
    stats_col.update_one(
        {"_id": group_id},
        {"$inc": {"messages": 1}},
        upsert=True
    )

def get_stats(group_id: int):
    doc = stats_col.find_one({"_id": group_id})
    if not doc:
        return {"user_joins": 0, "messages": 0}
    return {"user_joins": doc.get("user_joins", 0), "messages": doc.get("messages", 0)}
