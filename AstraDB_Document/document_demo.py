import requests

ASTRA_DB_ID = "" # your Astra DB ID
ASTRA_REGION = "" # e.g., us-east1, eu-west1
ASTRA_KEYSPACE = "" # Ensure this keyspace has a table with 'key' as primary key
ASTRA_TOKEN = "" # your application token

COLLECTION_URL = f"https://{ASTRA_DB_ID}-{ASTRA_REGION}.apps.astra.datastax.com/api/rest/v2/namespaces/{ASTRA_KEYSPACE}/collections/"

# --- Functions to manage collections ---

def CreateCollection(collection):
    url = COLLECTION_URL
    headers = {
        "X-Cassandra-Token": ASTRA_TOKEN,
        "Content-Type": "application/json"
    }
    payload = {
        "name": collection,
        "ifNotExists": True
    }
    print(url)
    response = requests.post(url, headers=headers, json=payload)
    print("Create Collection Status:", response.status_code)
    print("Create Collection Response:", response.text)

def GetCollections():
    url = COLLECTION_URL
    headers = {
        "X-Cassandra-Token": ASTRA_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    print("Get Collections Status:", response.status_code)
    print("Get Collections Response:", response.text)

def DeleteCollection(collecton):
    url = f"{COLLECTION_URL}/{collecton}"
    headers = {
        "X-Cassandra-Token": ASTRA_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)
    print("Delete Collection Status:", response.status_code)
    print("Delete Collection Response:", response.text)

# CreateCollection("restaurants")  #replace with your collection name
# GetCollections() 
# DeleteCollection("events") #replace with your collection name


# --- Functions to manage documents in a collection ---

# Sample document to insert
input = {
    "restaurant_name": "KFC",
    "address": {"street": "Main St", "city": "San Francisco", "state": "CA", "zip": 94105},
    "cuisine": "American",
    "rating": 4.5
    }

def CreateDocument(collection, document):
    url = f"{COLLECTION_URL}/{collection}"
    headers = {
        "X-Cassandra-Token": ASTRA_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=document)
    print("Create Document Status:", response.status_code)
    print("Create Document Response:", response.text)

def GetDocuments(collection):
    url = f"{COLLECTION_URL}/{collection}"
    headers = {
        "X-Cassandra-Token": ASTRA_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    print("Get Documents Status:", response.status_code)
    print("Get Documents Response:", response.text)

def GetDocumentById(collection, doc_id):
    url = f"{COLLECTION_URL}/{collection}/{doc_id}"
    headers = {
        "X-Cassandra-Token": ASTRA_TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    print("Get Document By ID Status:", response.status_code)
    print("Get Document By ID Response:", response.text)

# CreateDocument("restaurants", input)  #replace with your collection name
# GetDocuments("restaurants")  #replace with your collection name
# GetDocumentById("restaurants", "some-document-id")  #replace with your collection name and document id
