from pymongo import MongoClient


def get_db():
    client = MongoClient(
        host="127.0.0.1",
        port=27017,
        username="user",
        password="SuP3rS3cR3T",
        authSource="admin",
    )
    db = client["dnx"]
    return db

