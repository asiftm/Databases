# :memo: Astra Key-Value DB + Python Demo

This repository demonstrates how to interact with an **Astra Key-Value database** using **GraphQL** and **Python**.  
It includes basic operations such as insert (upsert), query by key, query all key-value pairs, and an attempted delete (note: Key-Value tables in Astra do not natively support delete mutations).

---

## 📂 Repository Contents

- `kv_graphql.py` – Python script demonstrating GraphQL operations on a Key-Value table.  

---

## 🛠️ Features

- Insert or upsert key-value pairs.
- Query a value by its key.
- Query all key-value pairs.
- Delete a key.

---

## ⚡ Requirements

- Python 3.x  
- `requests` library

Install `requests` via pip:

```bash
pip install requests
```

## 💡 References
:link: [GraphQL](https://graphql.org/learn/)

:link: [Datastax](https://www.datastax.com/)

:link: [AstraDB](https://www.datastax.com/products/datastax-astra)

:link: [Astra DB Serverless](https://docs.datastax.com/en/astra-db-serverless/index.html)

:link: [FreeCodeCamp Youtube Tutorial](https://youtu.be/xh4gy1lbL2k?si=_00BhbDIdw-TnhDF)


