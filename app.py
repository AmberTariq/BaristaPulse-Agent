import streamlit as st
import google.generativeai as genai

# 1. Setup the AI connection using your free key
# To test locally, you can paste your key here directly as a string: "AIzaSy..."
# (Later, we will secure this so no one steals it from GitHub!)
GOOGLE_API_KEY = "AQ.Ab8RN6KBAQEm_vLm2xtZw2GkugoyLn396wFra030aCMO5G_8oQ"
genai.configure(api_key=GOOGLE_API_KEY)

# 2. Your Aesthetic Header Design
st.title("☕ BaristaPulse: Your Aesthetic Coffee Agent")
st.write("Welcome to BaristaPulse, your personal coffee matchmaker! Tell me your mood or preference below.")

# 3. Create the Grid Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("💬 Conversation & Workspace")
    
    # This creates the text input box where users type
    user_mood = st.text_input("How are you feeling right now?", placeholder="e.g., I need a bold energetic boost...")

    # If the user types something and presses Enter, this trigger activates:
    if user_mood:
        with st.spinner("Analyzing your vibe... ☕"):
            try:
                # Tell the AI how it should behave
                system_instruction = (
                    "You are BaristaPulse, a warm and aesthetic personal coffee matchmaker. "
                    "Recommend the perfect coffee drink from a premium café menu that matches the customer's mood. "
                    "Keep your answer short, creative, and under 3 sentences."
                )
                
                # Combine the instruction with what the user typed
                full_prompt = f"{system_instruction}\n\nCustomer Mood: {user_mood}"
                
                # Call Google's fast, free model
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(full_prompt)
                
                # Display the AI's response inside a nice colored box
                st.write("✨ **BaristaPulse:**")
                st.info(response.text)
                
            except Exception as e:
                st.error(f"Something went wrong: {e}")

with col2:
    st.subheader("📋 Daily Signature Menu")
    st.write("- **Matcha Latte:** Creamy, smooth, and earthy.")
    st.write("- **Nitro Cold Brew:** Strong, bold, and energetic.")
    st.write("- **Vanilla Oat Macchiato:** Sweet and comforting.")
