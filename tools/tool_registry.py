from mcp_client.client import get_mcp_tools
from tools.base_tools import web_search, get_weather


async def get_tools():

    mcp_tools = await get_mcp_tools()

    tools = mcp_tools + [
        web_search,
        get_weather
    ]

    print(f"Loaded {len(tools)} tools")

    return tools