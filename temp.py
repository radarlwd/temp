from azure.cosmos import exceptions

def test_cosmos_connection():
    try:
        # Try to read the database
        _ = database.read()
        print("✅ Cosmos DB connected successfully.")
        return True
    except exceptions.CosmosHttpResponseError as e:
        print(f"❌ Failed to connect to Cosmos DB: {e}")
        return False


from azure.cosmos.exceptions import CosmosHttpResponseError

def test_cosmos_container_connection():
    try:
        # Try to read container metadata
        _ = container.read()
        print("✅ Cosmos container connected successfully.")
        return True
    except CosmosHttpResponseError as e:
        print(f"❌ Failed to connect to Cosmos container: {e}")
        return False
