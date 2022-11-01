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
client_games = client["Chess"]["created games"]
users_collection = client["Chess"]["users"]


# client = MongoClient("mongodb://localhost:27017/") # your connection string
# db = client["demo"]
# users_collection = db["users"]



class DataBaseInfo:

    @staticmethod
    def connect_db(games_or_users: str):
        # username = quote_plus(os.getenv("DB_USER_NAME"))
        # password = quote_plus(os.getenv("DB_PASSWORD"))
        # uri = f"mongodb+srv://{username}:{password}@maindata.sqlqx.mongodb.net/myFirstDatabase?retryWrites=true"
        # client = pymongo.MongoClient(uri)
        # return client["Chess"]["created games"]
        if games_or_users == "games":
            return client_games
        if games_or_users == "users":
            return users_collection


    @staticmethod
    def create_game(info: list):
        games = db_.connect_db("games")
        games.insert_one({"game": info})
        game_id = list(x for x in games.find({}))[-1]["_id"]
        return str(game_id)

    @staticmethod
    def get_game(game_id: str):
        return db_.connect_db("games").find_one({"_id": ObjectId(game_id)})["game"]

    @staticmethod
    def update_game(game_id: str, info: list):
        db_.connect_db("games").update_one({"_id": ObjectId(game_id)}, {"$set": {"game": info}})


db_ = DataBaseInfo()


