import pymongo
from pymongo import MongoClient 

Cluster = MongoClient("mongodb+srv://admin:admin123@cluster0.jvgl90b.mongodb.net/?appName=Cluster0")
db = Cluster["sldb"]
collection = db["employee"]

# Inserting multiple documents
posts = [
    {"name": "Bob", "age": 25, "email": "bob@gmail.com"},
    {"name": "Charlie", "age": 30, "email": "charlie@gmail.com"},
    {"name": "David", "age": 28, "email": "david@gmail.com"},
    {"name": "Virat", "age": 33, "email": "virat@gmail.com"},
    {"name": "Rohit", "age": 38, "email": "rohit@gmail.com"}

]

# collection.insert_many(posts)

# Reading data
# all_employees = collection.find()

# print("All employees:")
# for employee in all_employees:
#     print(employee)

# result = collection.find_one({"name": "Adam"})
# print("\nFind one result:")
# print(result)

# # Updating data
# collection.update_one({"name": "Bob"}, {"$set": {"age": 25}})
# collection.update_many({"age": {"$lt": 30}}, {"$set": {"status": "active"}})

# # Deleting data
# collection.delete_one({"name": "David"})
# collection.delete_many({"status": "inactive"})

# Printing final state
print("\nEmployees after updates and deletes:")
all_employees = collection.find()

for employee in all_employees:
    print(employee)
