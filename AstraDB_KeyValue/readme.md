# :memo: Astra Key-Value DB + Python Demo

This repository demonstrates how to interact with an **Astra Key-Value database** using **GraphQL** and **Python**.  
It includes basic operations such as insert (upsert), query by key, query all key-value pairs, and an attempted delete (note: Key-Value tables in Astra do not natively support delete mutations).

---

## :open_file_folder: Repository Contents

- :link: [kv_graphql.py](kv_graphql.py) – Python script demonstrating GraphQL operations on a Key-Value table.  

---

## :hammer_and_wrench: Features

- Insert or upsert key-value pairs.
- Query a value by its key.
- Query all key-value pairs.
- Delete a key.

---

## :zap: Requirements

- Python 3.x  
- `requests` library

Install `requests` via pip:

```bash
pip install requests
```
---
## :gear: Setup Instructions
1. Sign up using the official website [Datastax AstraDB](https://astra.datastax.com/signup)
2. Create a database using a free cloud provider and region.
3. It will take a moment to initialize a database.
4. Go to **Settings > Tokens**. Select role for example "**Database Administrator**" or "**Administrator User**" and an **Expiration** time to generate a token. Preview  permissions before generating to ensure accurate application access. Click on "**Generate Token**". **Download** or copy the secrets somewhere for future use.
5. Use **CQL Console** tab to run queries. Explore the collection, databases and features of  ***KeyValueDB***.
For example :
```
describe keyspaces; //to view all keyspaces
```
- :link: [Cassandra Query Language](https://cassandra.apache.org/doc/4.0/cassandra/cql/index.html)
- :link: [cqlsh: the CQL shell](https://cassandra.apache.org/doc/latest/cassandra/managing/tools/cqlsh.html)

6. Use **Connect** tab to explore options of connecting to the database.
7. Use secrets from token generation step to connect this database with :link: [kv_graphql.py](kv_graphql.py).
---
## :bulb: References
:link: [GraphQL](https://graphql.org/learn/)

:link: [Datastax](https://www.datastax.com/)

:link: [AstraDB](https://www.datastax.com/products/datastax-astra)

:link: [Astra DB Serverless](https://docs.datastax.com/en/astra-db-serverless/index.html)

:link: [FreeCodeCamp Youtube Tutorial](https://youtu.be/xh4gy1lbL2k?si=_00BhbDIdw-TnhDF)


