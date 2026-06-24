from langchain.tools import tool


@tool
def get_weather(city: str):
    """
    Get weather information.
    """
    return f"Weather for {city}"


@tool
def web_search(query: str):
    """
    Search latest information.
    """
    return f"Results for {query}"