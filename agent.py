import json
from google import adk

# 1. RAG function to securely load the database menu context
def view_coffee_menu():
    with open("menu.json", "r") as file:
        return json.load(file)

# 2. Build the official ADK core orchestrator agent
barista_agent = adk.agents.LlmAgent(
    name="BaristaPulse", 
    model="gemini-2.5-flash", 
    system_instruction=(
        "You are BaristaPulse, a warm, lively, and incredibly friendly coffee barista assistant. "
        "Always introduce yourself enthusiastically as BaristaPulse! Look at the menu tool provided "
        "and recommend a specific beverage matching the customer's mood or requests."
    ),
    tools=[view_coffee_menu]
)
