import asyncio
from dotenv import load_dotenv

from agents.hotel_agent import plan_trip

# Load environment variables from .env
load_dotenv()


async def ask():
    print("\nChat mode started. Type 'q' or 'quit' to exit.\n")

    while True:
        query = input("You: ").strip()

        if query.lower() in ["q", "quit"]:
            print("Exiting...")
            break

        await plan_trip(query)


if __name__ == "__main__":
    asyncio.run(ask())