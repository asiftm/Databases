# :memo: Astra Document API + Python Demo

This repository contains a simple Python project that demonstrates how to connect to **DataStax Astra DB** using the **Document API (JSON API)**. It performs basic CRUD operations on a `students` collection, showing how Astra can be used as a **document-oriented database** (similar to MongoDB).

---

## :open_file_folder: Repository Contents

- `document_demo.py` – Python script with few operations.  
---

## :hammer_and_wrench: Features

- Connect to Astra DB using the Document API (JSON API).  
- Create and manage a collection.  
- Insert single or multiple JSON documents.  
- Query all documents or find by ID.

---

## :zap: Requirements

- Python 3.x  
- Astra DB account + running database  
- Astra **Application Token** (secure connect credentials)  
- `requests` library  

Install dependencies via pip:

```bash
pip install requests
```
---
## :gear: Setup Instructions
1. Sign up using the official website [Datastax AstraDB](https://astra.datastax.com/signup)
2. Create a database using a free cloud provider and region.
3. It will take a moment to initialize a database.
4. Go to **Settings > Tokens**. Select role for example "**Database Administrator**" or "**Administrator User**" and an **Expiration** time to generate a token. Preview  permissions before generating to ensure accurate application access. Click on "**Generate Token**". **Download** or copy the secrets somewhere for future use.
5. Use **CQL Console** tab to run queries. Explore the collection, databases and features of  ***DocumentDB***.
For example :
```
describe keyspaces; //to view all keyspaces
```
- :link: [Cassandra Query Language](https://cassandra.apache.org/doc/4.0/cassandra/cql/index.html)
- :link: [cqlsh: the CQL shell](https://cassandra.apache.org/doc/latest/cassandra/managing/tools/cqlsh.html)

6. Use **Connect** tab to explore options of connecting to the database.
7. Use secrets from token generation step to connect this database with :link: [document_demo.py](document_demo.py).

---

## :bulb: References
:link: [Datastax](https://www.datastax.com/)

:link: [Cassandra Query Language](https://cassandra.apache.org/doc/4.0/cassandra/cql/index.html)

:link: [AstraDB](https://www.datastax.com/products/datastax-astra)

:link: [Astra DB Serverless](https://docs.datastax.com/en/astra-db-serverless/index.html)

:link: [FreeCodeCamp Youtube Tutorial](https://youtu.be/xh4gy1lbL2k?si=_00BhbDIdw-TnhDF)


