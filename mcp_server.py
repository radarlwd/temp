from mcp import MCPServer
from db import query_items

server = MCPServer(name="cosmosdb-mcp", description="MCP Server for Azure Cosmos DB")

@server.tool(name="query_cosmos", description="Execute a SQL query on Azure Cosmos DB")
async def query_cosmos(arguments: dict) -> list:
    query = arguments.get("query")
    if not query:
        return {"error": "No query provided."}
    try:
        results = query_items(query)
        return results
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    server.run()
