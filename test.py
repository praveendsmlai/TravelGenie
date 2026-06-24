from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

async def main():
    client = MultiServerMCPClient({
        "google-calendar": {
            "command": "npx",
            "args": ["@cocal/google-calendar-mcp"],
            "env": {
                "GOOGLE_OAUTH_CREDENTIALS":
                r"C:\Users\pulip\.gmail-mcp\gcp-oauth.keys.json"
            },
            "transport": "stdio"
        }
    })

    tools = await client.get_tools()
    print(tools)

asyncio.run(main())