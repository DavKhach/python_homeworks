import json
from datetime import datetime
from passlib.context import CryptContext

from model import User
from config import Config


config = Config()
pwd_context = CryptContext(schemes="sha256_crypt")

def _initialize_users_db():
    try:
        with open(config.FILE_PATH, "x") as file:
            json.dump({}, file)
    except FileExistsError:
        pass

def _read_user_db():
    users_file = config.FILE_PATH[0]
    try:
        with open(users_file) as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


def _write_users_db(users):
    users_file = config.FILE_PATH[0]
    with open(users_file, "w") as file:
        json.dump(users, file, indent=2)

def log_activity(event_type: str, username: str, status: str = None):
    try:
        with open("logs.json", "r") as file:
            logs = json.loads(file.read() or "[]")
    except FileNotFoundError:
        logs = []

    log_entry = {
        "event": event_type,
        "username": username,
        "timestamp": datetime.now().isoformat()
    }
    if status:
        log_entry["status"] = status
    logs.append(log_entry)

    with open("logs.json", "w") as file:
        json.dump(logs, file, indent=2)

def register_user(user: User):
    db = _read_user_db()
    if user.username in db:
        return False

    hashed_password = pwd_context.hash(user.password)
    db[user.username] = {"username": user.username, "password": hashed_password}

    _write_users_db(db)
    return True

def authenticate_user(user: User)-> bool:
    db = _read_user_db()
    user_data = db.get(user.username)

    if not user_data:
        log_activity("login", user.username, status="failure")
        return False

    if not pwd_context.verify(user.password, user_data["password"]):
        log_activity("login", user.username, status="failure")
        return False

    log_activity("login", user.username, status="success")
    return True
