import json


def load_mcp_config(*servers):

    with open("config/mcp_config.json") as f:
        config = json.load(f)

    return {
        server: config[server]
        for server in servers
    }