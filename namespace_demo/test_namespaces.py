import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Setup
async def main():
    session_service = InMemorySessionService()

    session = await session_service.create_session(
        app_name="namespace_demo_app",
        user_id="user1",
        session_id="session1"
    )
    
    runner = Runner(
        agent=root_agent,
        app_name="namespace_demo_app",
        session_service=session_service
    )

    # Set all four namespace types
    print("=== Setting state in all namespaces ===")
    session.state["app:name"] = "Namespace Demo"
    session.state["app:version"] = "2.0"
    session.state["user:theme"] = "dark"
    session.state["topic"] = "state management"
    session.state["temp:step"] = "initialization"  # Changed from temp:state to temp:step to match your print statements below

    print(f"State before run: {session.state}\n")

    # Run agent (Turn 1)
    print("=== Running agent (Turn 1) ===")
    async for event in runner.run_async(
        user_id="user1",
        session_id="session1",
        new_message=Content(parts=[Part(text="Show me the namespace values")])
    ):
        # Indented properly and defensive checks added
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Agent response: \n{event.content.parts[0].text}\n")

    # Check state after turn
    print("=== State after Turn 1 ===")
    print(f"Full state: {session.state}")
    print(f"temp:step: {session.state.get('temp:step')}")
    print(f"topic: {session.state.get('topic')}")
    print(f"user:theme: {session.state.get('user:theme')}")
    print(f"app:version: {session.state.get('app:version')}")

    print("\n=== Simulating Turn 2 (same session) ===")
    
    # Changed run to run_async and added async before for
    async for event in runner.run_async(
        user_id="user1",
        session_id="session1",
        new_message=Content(parts=[Part(text="Check state again")])
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Agent response:\n{event.content.parts[0].text}\n")

    print("=== State after Turn 2 ===")
    print(f"Full state: {session.state}")
    print(f"temp:step: {session.state.get('temp:step')}")
    print(f"topic: {session.state.get('topic')}")
    print(f"user:theme: {session.state.get('user:theme')}")

    # Simulate new session
    print("\n=== Simulating NEW Session (session2) ===")
    
    # Added missing await
    session2 = await session_service.create_session(
        app_name="namespace_demo_app",
        session_id="session2", 
        user_id="user1" 
    )

    print(f"New Session state: {session2.state}")
    print(f"topic: {session2.state.get('topic')}")
    print(f"user:theme: {session2.state.get('user:theme')}")
    print(f"app:version: {session2.state.get('app:version')}")

if __name__ == "__main__":
    asyncio.run(main())