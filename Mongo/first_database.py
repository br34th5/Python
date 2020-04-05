import pymongo
from pymongo import MongoClient



myClient = MongoClient()
db = myClient.mydb

#in mongo Table is called collection:
users = db.users
user1 = {"username": "Einaras", "password": "123aasd", 
         "favorite_number": 8, 
         "hobbies": ["python", "gaming", "fitness"]
         }
#methods of a collection:
user_id = users.insert_one(user1).inserted_id
user_id