import streamlit as st
import json

# Set up page configurations with a friendly coffee emoji
st.set_page_config(page_title="BaristaPulse AI", page_icon="☕", layout="wide")

# Expanded Dataset directly embedded to avoid separate file read crashes
@st.cache_data
def load_expanded_menu():
    return [
        {"name": "Matcha Latte", "vibe": "creamy, smooth, and earthy", "sizes": ["Small", "Medium", "Large"], "milks": ["Whole Milk", "Oat", "Almond"], "syrups": ["None", "Vanilla"]},
        {"name": "Nitro Cold Brew", "vibe": "strong, bold, and highly energetic", "sizes": ["Medium", "Large"], "milks": ["None", "Splash of Oat"], "syrups": ["None", "Vanilla"]},
        {"name": "Vanilla Oat Macchiato", "vibe": "sweet, warm, and comforting", "sizes": ["Small", "Medium", "Large"], "milks": ["Oat"], "syrups": ["Vanilla", "Caramel"]},
        {"name": "Lavender Dream Latte", "vibe": "calming, floral, and deeply relaxing", "sizes": ["Small", "Medium", "Large"], "milks": ["Almond", "Oat"], "syrups": ["Lavender", "Vanilla"]},
        {"name": "Salted Caramel Affogato", "vibe": "indulgent, sweet, and dessert-like", "sizes": ["Small"], "milks": ["Ice Cream Base"], "syrups": ["Salted Caramel"]}
    ]

menu = load_expanded_menu()

# Initialize session structures for Favorites and History tracking
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "order_history" not in st.session_state:
    st.session_state.order_history = []
if "current_recommendation" not in st.session_state:
    st.session_state.current_recommendation = None

# Sidebar Panels
with st.sidebar:
    st.header("👤 BaristaPulse Profile")
    st.subheader("⭐ Saved Favorites")
    if st.session_state.favorites:
        for fav in st.session_state.favorites:
            st.markdown(f"- **{fav}**")
    else:
        st.caption("No favorites saved yet.")
        
    st.subheader("📜 Order History")
    if st.session_state.order_history:
        for past in reversed(st.session_state.order_history):
            st.markdown(f"**{past['item']}** ({past['size']})")
    else:
        st.caption("Your tray is empty.")

# Main Application Headers
st.title("☕ BaristaPulse: Aesthetic Coffee Agent ✨")
st.write("Welcome! I am BaristaPulse, your personal coffee matchmaker. Tell me your mood or taste preference below!")

col1, col2 = st.columns(2)

with col1:
    vibe_input = st.text_input("How are you feeling right now?", placeholder="e.g., I need a bold boost or something calming...")
    if vibe_input:
        matched_drink = menu[0] # Default fallback rule
        for drink in menu:
            if any(word in vibe_input.lower() for word in drink["vibe"].replace(",", "").split()):
                matched_drink = drink
                break
        st.session_state.current_recommendation = matched_drink
        
        st.markdown(f"""
        **BaristaPulse:** "Hey there! Based on your preference, I highly recommend our **{matched_drink['name']}**! 
        It is crafted to be exceptionally *{matched_drink['vibe']}*."
        """)

with col2:
    if st.session_state.current_recommendation:
        drink = st.session_state.current_recommendation
        st.subheader(f"🎨 Customize {drink['name']}")
        
        chosen_size = st.selectbox("Size:", drink["sizes"])
        chosen_milk = st.selectbox("Milk:", drink["milks"])
        chosen_syrup = st.selectbox("Syrup:", drink["syrups"])
        
        if st.button("⭐ Add to Favorites"):
            if drink["name"] not in st.session_state.favorites:
                st.session_state.favorites.append(drink["name"])
                st.rerun()
                
        if st.button("🛒 Place Cafe Order"):
            st.session_state.order_history.append({"item": drink["name"], "size": chosen_size})
            st.success(f"BaristaPulse is prepping your custom {drink['name']}!")
            st.rerun()
