from pymongo import MongoClient
import os


def get_db():
    client = MongoClient(
        host=os.getenv("MONGO_HOST"),
        port=os.getenv("MONGO_PORT"),
        username=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
        authSource="admin",
    )
    db = client[os.getenv("MONGO_DATABASE")]
    return db
