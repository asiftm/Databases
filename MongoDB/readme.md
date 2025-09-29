# :memo: MongoDB + Python Demo

This repository contains a short and simple ***Python*** project that demonstrates how to connect to ***MongoDB***, perform basic CRUD operations, and manage a student collection. It uses ***PyMongo*** to interact with both local ***MongoDB*** instances and ***MongoDB Atlas***.

---

## :open_file_folder: Repository Contents

- `mongodb_demo.py` – Python script with full CRUD operations (insert, query, update, delete).  
- `students.json` – Sample JSON data (optional).  

---

## :hammer_and_wrench: Features

- Connect to MongoDB (local or Atlas cloud).  
- Create and drop collections.  
- perform basic CRUD operations 

---

## :zap: Requirements

- Python 3.x  
- MongoDB (local or Atlas)  
- PyMongo library
- MongoDB Compass (optional)

Install PyMongo via pip:

```bash
pip install pymongo
```

## :gear: Setup Instructions
1. Download and install [MongoDB Community Server](https://www.mongodb.com/try/download/community).
2. Download and install [MongoDB Compass](https://www.mongodb.com/products/tools/compass), the **GUI** for **MongoDB**
3. Open **MongoDB Compass** and use an exting connection or create a new connection.
4. Create a database in the connection.
5. Create a collection in the database.
6. Import :link: [Student JSON Data](school.students.json) into the collection or copy the :link: [Student JSON Data](school.students.json) file and paste.
7. Use **MongoDB Compass GUI** to explore the data.

- :link: [MongoDB Official Docs](https://www.mongodb.com/docs/)

- :link: [MongoDB Query Documents](https://www.mongodb.com/docs/manual/tutorial/query-documents/)

8. Use your connection host URL to connect this database with :link: [mongodb_demo.py](mongodb_demo.py).

---

## :bulb: References
:link: [MongoDB Official Docs](https://www.mongodb.com/docs/)

:link: [PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)

:link: [MongoDB Compass](https://www.mongodb.com/products/tools/compass)

:link: [BroCode Youtube Tutorial](https://www.youtube.com/watch?v=c2M-rlkkT5o&t=3481s)



