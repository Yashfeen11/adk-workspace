import os
from dotenv import load_dotenv

# Yeh function tumhari .env file ko dhundhega aur API key environment mein load kar dega
load_dotenv() 

import asyncio
from agent import root_agent

import asyncio
from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

async def main():
    # 1. Initialize session storage
    session_service = InMemorySessionService()

    # 2. CREATE SESSION (await is mandatory)
    session = await session_service.create_session(
        app_name="greeter_app",
        user_id="user1",
        session_id="session1"
    )

    # 3. Setup Runner
    runner = Runner(
        agent=root_agent,
        app_name="greeter_app",
        session_service=session_service
    )

    # --- TEST 1: NO STATE (DEFAULTS) ---
    print("=== Test 1: No state (all defaults) ===")
    async for event in runner.run_async(
        user_id="user1",
        session_id="session1",
        new_message=Content(parts=[Part(text="Hello")])
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Agent: {event.content.parts[0].text}\n")


    # --- TEST 2: WITH USER NAME ---
    print("=== Test 2: With user name ===")
    
    # State update directly via dictionary before running agent
    session.state["user_name"] = "Yashfeen"
    
    # Since ADK saves state in memory, we update it via the service 
    # to ensure the runner sees the new manual changes

    async for event in runner.run_async(
        user_id="user1",
        session_id="session1",
        new_message=Content(parts=[Part(text="Hello again")])
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Agent: {event.content.parts[0].text}\n")


    # --- TEST 3: WITH ALL STATE VALUES ---
    print("=== Test 3: With all state values ===")
    
    session.state["user_name"] = "Yashfeen"
    session.state["user_language"] = "Hindi"
    session.state["membership_tier"] = "premium"


    async for event in runner.run_async(
        user_id="user1",
        session_id="session1",
        new_message=Content(parts=[Part(text="Hello")])
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(f"Agent: {event.content.parts[0].text}\n")

    # Verify final state
    print("=== Current state ===")
    print(session.state)

if __name__ == "__main__":
    asyncio.run(main())