from langchain.agents import create_agent
from langchain.messages import HumanMessage

from models.llm import get_llm
from tools.tool_registry import get_tools
from prompts.hotel_prompt import get_travel_planner_prompt
from langgraph.checkpoint.memory import InMemorySaver


async def plan_trip(query: str, thread_id="default"):

    llm = get_llm()

    tools = await get_tools()

    system_prompt = get_travel_planner_prompt()


    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
        checkpointer=InMemorySaver()
    )

    config = {"configurable": {"thread_id": thread_id}}

    result = await agent.ainvoke(
        {
            "messages": [
                HumanMessage(query)
            ]
        },config=config
    )

    response = result["messages"][-1].text

    print("\n========================")
    print(response)
    print("========================")