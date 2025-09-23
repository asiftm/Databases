import requests

ASTRA_DB_ID = "" # your Astra DB ID
ASTRA_REGION = "" # e.g., us-east1, eu-west1
ASTRA_KEYSPACE = "" # Ensure this keyspace has a table with 'key' as primary key
ASTRA_TOKEN = "" # your application token
GRAPHQL_URL = f"https://{ASTRA_DB_ID}-{ASTRA_REGION}.apps.astra.datastax.com/api/graphql/{ASTRA_KEYSPACE}"

headers = {
    "x-cassandra-token": ASTRA_TOKEN,
    "Content-Type": "application/json"
}

# lets say we have a table `shop_inventory` with columns `key` (primary key) and `value` in the `keyvalue` keyspace.
#     key |   value
#  --------+---------
#  42dhww | shampoo
#   3rd53 |   beans



# --- Insert key-value pair ---
def PostGraphQL(key, value):
    mutation = """
    mutation InsertItem($k: String!, $v: String!) {
      insertshop_inventory(
        value: {key: $k, value: $v}
      ) {
        applied
      }
    }
    """
    variables = {"k": key, "v": value}
    r = requests.post(GRAPHQL_URL, headers=headers, json={"query": mutation, "variables": variables})
    print("Insert Response:", r.json())

# PostGraphQL("8ads4", "Milk")



# # --- Query value by key ---
def QueryGraphQL(key):
    query = """
    query GetByKey($k: String!) {
      shop_inventory(filter: {key: {eq: $k}}) {
        values {
          key
          value
        }
      }
    }
    """
    variables = {"k": key}
    r = requests.post(GRAPHQL_URL, headers=headers, json={"query": query, "variables": variables})
    print("Query Response:", r.json())

# QueryGraphQL("7dfg4")



# ---- Query all key-value pairs ----
def GetAllGraphQL():
    query_all = """
      query {
        shop_inventory {
          values{
            key,
            value
          }
        }
      }
      """
    r = requests.post(GRAPHQL_URL, headers=headers, json={"query": query_all})
    print("All Key-Values:", r.json())

# GetAllGraphQL()


# --- Delete key-value pair by key ---
def DeleteGraphQL(key):
    mutation = """
    mutation DeleteItem($k: String!) {
      deleteshop_inventory(
        value: {key: $k}
      ) 
      { value {
              key
        }
      }
    }
    """
    variables = {"k": key}
    r = requests.post(GRAPHQL_URL, headers=headers, json={"query": mutation, "variables": variables})
    print("Delete Response:", r.json())

# DeleteGraphQL("3rd53")
