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
students = [{"name":"Patrick", "age":38, "gpa": 1.5},  
            {"name":"Sandy", "age":27, "gpa": 4.0},
            {"name":"Gary", "age":18, "gpa": 2.5}]

# ----- Functions -----
    

def create_collection():
    db.create_collection("students")

def drop_collection():
    collection.drop()

def add_student(student):
    insert_result = collection.insert_one(student)
    print("Inserted document ID:", insert_result.inserted_id)

def insert_multiple(students):
    insert_result = collection.insert_many(students)
    print("Inserted document IDs:", insert_result.inserted_ids)

def find_student(name):
  results = collection.find({"name": name})
  for doc in results:
      print(doc)

def all_students():
    for doc in collection.find():
        print(doc)

# ----- Usage -----
# open_connecton()
# create_collection()
# drop_collection()
# insert_multiple(students)
# add_student(student)
# find_student("Asif")
# all_students()
# client.close()







