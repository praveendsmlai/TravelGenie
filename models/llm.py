from langchain_openai import ChatOpenAI


def get_llm():
    return ChatOpenAI(
        model="gpt-5.4-mini"
    )