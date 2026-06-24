from langchain_mcp_adapters.client import MultiServerMCPClient
from utils.utils import load_mcp_config


async def get_mcp_tools():

    mcp_config = load_mcp_config(
        "airbnb",
        "google-calendar"
    )

    client = MultiServerMCPClient(mcp_config)

    return await client.get_tools()