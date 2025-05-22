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
