import settings

from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "server_rag": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.server_rag_mcp_tool]
        },
        "server_api": {
            "transport": "stdio",
            "command": "python",
            "args": [settings.server_api_mcp_tool]
        }
    }
)