import streamlit as st
import json

# Apply structural configurations first
st.set_page_config(page_title="BaristaPulse AI", page_icon="☕", layout="wide")

# Custom styling wrapper block
st.markdown("""
    <style>
    .stApp {
        background-color: #FFFDD0;
    }
    h1, h2, h3, p, label, .stMarkdown {
        color: #4A2E1B !important;
    }
    .stButton>button {
        background-color: #4A2E1B !important;
        color: #FFFDD0 !important;
        border-radius: 8px;
    }
    .drink-card {
        background-color: #FFF8E7;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_html=True)

# Dataset initializer function
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

# Establish memory storage variables
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "order_history" not in st.session_state:
    st.session_state.order_history = []
if "current_recommendation" not in st.session_state:
    st.session_state.current_recommendation = None

# Sidebar panels
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

# Main screen conversation layout panels
st.title("☕ BaristaPulse: Aesthetic Coffee Agent ✨")
st.write("Welcome! I am **BaristaPulse**, your personal coffee matchmaker. Tell me your mood or taste preference below!")

col1, col2 = st.columns(2)

with col1:
    vibe_input = st.text_input("How are you feeling right now?", placeholder="e.g., I need a bold boost or something calming...")
    if vibe_input:
        matched_drink = menu[0] # Default fallback matching rule
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
