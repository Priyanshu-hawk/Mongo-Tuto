from utils import mongo_db_connection

mongo_obj =  mongo_db_connection("test_db")

# mongo_id = mongo_obj.insert_one("test_collection", {"name": "test_name", "age": 20})

# print(mongo_id)

new_data = {"name": "new_name", "age": 30}

mongo_obj.update_by_mongo_id("test_collection", "66c98feaea00ba936ae0bebf", new_data)