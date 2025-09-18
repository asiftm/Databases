from pymongo import MongoClient
from datetime import datetime

# ----- Connection -----
# For local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# For MongoDB Atlas (replace <username>, <password>, and <cluster_url>)
# client = MongoClient("mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/")

# ----- Database -----
db = client["school"]   # create/use a database called test_db

# ----- Collection -----
collection = db["students"]   # create/use a collection called students

# ----- Insert a document -----
student = {"name": "Asif", "course": ["Data Science"], "graduationDate": datetime(2023, 6, 15)}

def add_student(student):
    insert_result = collection.insert_one(student)
    print("Inserted document ID:", insert_result.inserted_id)

def find_student(name):
  print("document:", collection.find({"name": "Asif"}))

def all_students():
    print("All documents:")
    for doc in collection.find():
        print(doc)

