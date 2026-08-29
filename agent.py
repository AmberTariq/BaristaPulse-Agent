import json
import os
from google import genai
from google.genai import types
import streamlit as st

# Retrieve the API Key seamlessly from your Streamlit Secrets vault
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

def view_coffee_menu():
    with open("menu.json", "r") as file:
        return json.load(file)

class CustomBaristaAgent:
    def __init__(self):
        self.name = "BaristaPulse"
        self.model = "gemini-2.5-flash"
        self.system_instruction = (
            "You are BaristaPulse, a warm, lively, and incredibly friendly coffee barista assistant. "
            "Always introduce yourself enthusiastically as BaristaPulse! Recommend a specific beverage "
            "matching the customer's mood or requests from your menu data tool context."
        )

    def run(self, user_input):
        menu_context = view_coffee_menu()
        prompt = f"""
        System Context: {self.system_instruction}
        Available Menu Items: {json.dumps(menu_context)}
        
        Customer Input: "{user_input}"
        
        Respond friendly as BaristaPulse and make your tailored recommendation:
        """
        response = client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return response

barista_agent = CustomBaristaAgent()
