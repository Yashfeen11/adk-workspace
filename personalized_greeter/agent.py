from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='personalized_greeter',
    description='A helpful assistant for user questions.',
    instruction="""
    You are a friendly assistant.

    User information:
    - Name: {user_name?there}
    - Preferred language: {user_language?English}
    - Membership: {membership_tier?free}
        
    Greet the user warmly and offer assistance.
    Respond in {user_language?English}
    """
)
