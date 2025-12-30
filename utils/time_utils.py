from datetime import datetime, timedelta

def add_seconds_to_now(seconds: int):
    return datetime.now() + timedelta(seconds=seconds)

def add_minutes_to_now(minutes: int):
    return datetime.now() + timedelta(minutes=minutes)

def add_hours_to_now(hours: int):
    return datetime.now() + timedelta(hours=hours)

def format_datetime(dt: datetime, fmt: str = "%d-%m-%Y %H:%M:%S"):
    return dt.strftime(fmt)
