import os, datetime
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["soulence_db"]
chat_collection = db["chats"]

def save_chat(user_id, user_msg, bot_reply, mood):
    chat_collection.insert_one({
        "user_id": user_id,
        "user_message": user_msg,
        "bot_reply": bot_reply,
        "mood": mood,
        "timestamp": datetime.datetime.utcnow()
    })

def get_history(user_id):
    return list(chat_collection.find({"user_id": user_id}, {"_id": 0}))
