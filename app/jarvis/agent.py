from google.adk.agents import Agent
from prompt import ROOT_AGENT_INSTRUCTION
root_agent = Agent(
    name="jarvis",
    description="An emergency services agent",
    instruction=ROOT_AGENT_INSTRUCTION
)