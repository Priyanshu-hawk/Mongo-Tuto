from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi
import os
from dotenv import load_dotenv
load_dotenv()

class mongo_db_connection():
    def __init__(self, db_name):
        self.uri = os.getenv("MONGO_URI")
        self.ca = certifi.where()
        self.client = MongoClient(self.uri, tlsCAFile=self.ca)
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        self.db = self.client[db_name]

    def insert_one(self, collection_name, item):
        collection = self.db[collection_name]
        mongo_id = collection.insert_one(item)
        return mongo_id.inserted_id
    
    def get_all(self, collection_name):
        collection = self.db[collection_name]
        all_items = collection.find()
        return all_items

    def delete_item(self, collection_name, item):
        collection = self.db[collection_name]
        collection.delete_one(item)

    def find_one_by_uiqu_id(self, collection_name, id):
        all_items = self.get_all(collection_name)
        for item in all_items:
            if id in item:
                return item
        return None
    
    def find_one_by_key_value(self, collection_name, key, value):
        collection = self.db[collection_name]
        return collection.find_one({key: value})

    def find_one_by_mongo_id(self, collection_name, mongo_id):
        collection = self.db[collection_name]
        return collection.find_one({"_id": ObjectId(mongo_id)})

    def is_uiqu_id_exist(self, collection_name, id):
        all_items = self.get_all(collection_name)
        for item in all_items:
            if id in item:
                return True
        return False
    
    def update_by_mongo_id(self, collection_name, mongo_id, new_json):
        collection = self.db[collection_name]
        collection.update_one({"_id": ObjectId(mongo_id)}, {"$set": new_json})