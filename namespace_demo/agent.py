"""
Name space Demo - Shows all four state namespaces
Demonstrate temp, session, user, app: prsistence scopers.
Reference: https://google.github.io/adk-docs/sessions/state.md

"""

from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='namespace_demo',
    description='A helpful assistant for user questions.',
    instruction=""" 
    You are a demo assistant showing state namespaces.

    === App State (global for all users)    
        App name: {app:name?Namespace Demo}
        App version: {app:version?1.0}

    === User State (persists across sessions) ===
        User preference: {user:theme?not set}
    
    === Session State (persists this conversation) ===
       Conversation topic: {topic?not set}

    === Temp State (current turn only) 
        Current step: {temp:step?not set}

    Respond with a friendly message showing these namespace values.
""",
output_key="response"
)
