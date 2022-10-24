import os
import pymongo
from urllib.parse import quote_plus
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()
username = quote_plus(os.getenv("DB_USER_NAME"))
password = quote_plus(os.getenv("DB_PASSWORD"))
uri = f"mongodb+srv://{username}:{password}@maindata.sqlqx.mongodb.net/myFirstDatabase?retryWrites=true"
client = pymongo.MongoClient(uri)
client = client["Chess"]["created games"]


class DataBaseInfo:

    @staticmethod
    def connect_db():
        # username = quote_plus(os.getenv("DB_USER_NAME"))
        # password = quote_plus(os.getenv("DB_PASSWORD"))
        # uri = f"mongodb+srv://{username}:{password}@maindata.sqlqx.mongodb.net/myFirstDatabase?retryWrites=true"
        # client = pymongo.MongoClient(uri)
        # return client["Chess"]["created games"]
        return client

    @staticmethod
    def create_game(info: list):
        games = db_.connect_db()
        games.insert_one({"game": info})
        game_id = list(x for x in games.find({}))[-1]["_id"]
        return str(game_id)

    @staticmethod
    def get_game(game_id: str):
        return db_.connect_db().find_one({"_id": ObjectId(game_id)})["game"]

    @staticmethod
    def update_game(game_id: str, info: list):
        db_.connect_db().update_one({"_id": ObjectId(game_id)}, {"$set": {"game": info}})


db_ = DataBaseInfo()


