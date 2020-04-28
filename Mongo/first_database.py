import pymongo
from pymongo import MongoClient



myClient = MongoClient()
db = myClient.mydb

#in mongo, Table is called collection:
users = db.users
user1 = {"username": "Einaras", "password": "123aasd", 
         "favorite_number": 8, 
         "hobbies": ["python", "gaming", "fitness"]
         }
#methods of a collection:
user_id = users.insert_one(user1).inserted_id
users = [{"username": "corsair", "password": "12345"},
         {"username": "msi", "password": "red"}]

logins = db.users
"""
inserted = logins.insert_many(users)
inserted.inserted_ids
inserted.inserted_ids

logins.find().count()
logins.find({"favorite_number": 8}).count()
logins.find({"favorite_number": 8, "username": "Einaras"}).count()
"""

#more efficient way to search:
db.users.create_index([("username", pymongo.ASCENDING)])
logins.find({"username": "Einaras"})
