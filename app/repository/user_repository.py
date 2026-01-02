from app.db.mongo import db
from bson import ObjectId

collection = db.users

class UserRepository:

    def create(self, user: dict):
        result = collection.insert_one(user)
        return str(result.inserted_id)

    def find_all(self):
        users = []
        for u in collection.find():
            u["id"] = str(u["_id"])
            del u["_id"]
            users.append(u)
        return users

    def find_by_id(self, user_id: str):
        user = collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            return None
        user["id"] = str(user["_id"])
        del user["_id"]
        return user

    def update(self, user_id: str, data: dict):
        collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": data}
        )

    def delete(self, user_id: str):
        collection.delete_one({"_id": ObjectId(user_id)})
