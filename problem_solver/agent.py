from google.adk.agents.llm_agent import Agent
from google.adk.planners import BuiltInPlanner
from google.genai import types

root_agent = Agent(
    model='gemini-3.5-flash',
    name='strategic-problem-solver',
    description='Solves complex problems using multi-step reasoning and planning',
    instruction="""You are a strategic Problem Solver.
    Your approach to complex problems:
    1. **Understand** - Break down the problem into components
    2. **Analyze** - Consider multiple approaches and trade-offs
    3. **Plan** - Develop a step-by-step solution strategy
    4. **Execute** - Provide clear, actionable recommendations
    For complex problems:- Think through implications and edge cases- Consider short-term vs long-term consequences- Identify potential risks and mitigation strategies- Provide reasoning for your recommendations
    
    Be thorough, analytical, and systematic in your approach.""",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True,
            thinking_budget=2048
        )
    )

)
