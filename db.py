import os
from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv

load_dotenv()

COSMOS_ENDPOINT = os.getenv("COSMOS_ENDPOINT")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = os.getenv("COSMOS_DATABASE")
CONTAINER_NAME = os.getenv("COSMOS_CONTAINER")

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.create_database_if_not_exists(id=DATABASE_NAME)
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME,
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)

def run_query(sql_query: str):
    try:
        return list(container.query_items(query=sql_query, enable_cross_partition_query=True))
    except Exception as e:
        return {"error": str(e)}
