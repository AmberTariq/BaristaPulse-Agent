import streamlit as st
import json

# Set up page configurations with your aesthetic theme colors
st.set_page_config(page_title="BaristaPulse AI", page_icon="☕", layout="wide")

# Custom CSS injection for the soft cream background and warm coffee-brown vibe
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
        border: none;
    }
    .stButton>button:hover {
        background-color: #6F4E37 !important;
        color: #FFFDD0 !important;
    }
    .drink-card {
        background-color: #FFF8E7;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #E6D2B8;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_html=True)

# --- FEATURE 1: EXPANDED MOCK DATASET ---
@st.cache_data
def load_expanded_menu():
    return [
        {
            "name": "Matcha Latte",
            "vibe": "creamy, smooth, and earthy",
            "sizes": ["Small", "Medium", "Large"],
            "milks": ["Whole Milk", "Oat", "Almond", "Soy"],
            "syrups": ["None", "Vanilla", "Matcha Sweetener"]
        },
        {
            "name": "Nitro Cold Brew",
            "vibe": "strong, bold, and highly energetic",
            "sizes": ["Medium", "Large"],
            "milks": ["None", "Splash of Oat", "Splash of Almond"],
            "syrups": ["None", "Vanilla", "Caramel"]
        },
        {
            "name": "Vanilla Oat Macchiato",
            "vibe": "sweet, warm, and comforting",
            "sizes": ["Small", "Medium", "Large"],
            "milks": ["Oat"],
            "syrups": ["Vanilla", "Caramel"]
        },
        {
            "name": "Rose Gold Espresso Tonic",
            "vibe": "bubbly, floral, and experimental",
            "sizes": ["Small", "Medium"],
            "milks": ["None"],
            "syrups": ["Rose Infusion", "Simple Syrup"]
        },
        {
            "name": "Lavender Dream Latte",
            "vibe": "calming, floral, and deeply relaxing",
            "sizes": ["Small", "Medium", "Large"],
            "milks": ["Almond", "Oat", "Coconut"],
            "syrups": ["Lavender Bark", "Vanilla"]
        },
        {
            "name": "Spiced Cardamom Cortado",
            "vibe": "intense, aromatic, and sophisticated",
            "sizes": ["Small"],
            "milks": ["Whole Milk", "Oat"],
            "syrups": ["Cardamom Spice", "Brown Sugar"]
        },
        {
            "name": "Salted Caramel Affogato",
            "vibe": "indulgent, sweet, and dessert-like",
            "sizes": ["Small"],
            "milks": ["Vanilla Ice Cream Base"],
            "syrups": ["Salted Caramel Drizzle"]
        },
        {
            "name": "Mocha Velvet Frappe",
            "vibe": "icy, rich, chocoholic, and fun",
            "sizes": ["Medium", "Large"],
            "milks": ["Whole Milk", "Oat", "Soy"],
            "syrups": ["Dark Chocolate Sauce", "Hazelnut"]
        }
    ]

menu = load_expanded_menu()

# Initialize session structures for Favorites and Order History
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "order_history" not in st.session_state:
    st.session_state.order_history = []
if "current_recommendation" not in st.session_state:
    st.session_state.current_recommendation = None

# --- SIDEBAR INTERFACE: USER PROFILE, FAVORITES & HISTORY ---
with st.sidebar:
    st.header("👤 BaristaPulse User Profile")
    st.write("Managing your current active cafe session safely.")
    
    # FEATURE 2: FAVORITES VIEW
    st.subheader("⭐ My Saved Favorites")
    if st.session_state.favorites:
        for fav in st.session_state.favorites:
            st.markdown(f"- **{fav}**")
    else:
        st.caption("No favorites saved yet. Chat with the barista below to add options!")
        
    # FEATURE 3: SESSION ORDER HISTORY VIEW
    st.subheader("📜 Past Order History")
    if st.session_state.order_history:
        for idx, past_order in enumerate(reversed(st.session_state.order_history)):
            st.markdown(f"**{past_order['item']}**")
            st.caption(f"Config: {past_order['size']} | {past_order['milk']} | {past_order['syrup']} | {past_order['extra']}")
            if st.button(f"Reorder This", key=f"reorder_{idx}"):
                st.session_state.order_history.append(past_order)
                st.success(f"Successfully re-ordered your {past_order['item']}!")
                st.rerun()
    else:
        st.caption("Your order tray is currently empty.")

# --- MAIN PAGE CONTEXT INTERFACE ---
st.title("☕ BaristaPulse: Aesthetic Conversation Engine ✨")
st.write("Tell us your mood, get recommendations, and tailor your perfect drink formula.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💬 Chat with BaristaPulse")
    vibe_input = st.text_input("How are you feeling right now? Describe your flavor profile or mood:", 
                               placeholder="e.g., I need a rich chocoholic treat or something relaxing and floral...")

    if vibe_input:
        # Simplistic intent router matching input strings to the expanded JSON dictionary objects
        matched_drink = None
        for drink in menu:
            if any(word in vibe_input.lower() for word in drink["vibe"].replace(",", "").split()):
                matched_drink = drink
                break
        
        # Fallback default choice if no target vocabulary hits match exactly
        if not matched_drink:
            matched_drink = menu[0]
            
        st.session_state.current_recommendation = matched_drink
        
        # Verbose response simulation introducing the agent identity clearly
        st.markdown(f"""
        **BaristaPulse:** "Hey there! I am **BaristaPulse**, your personal coffee matchmaker! 🌟 
        Based on your current mood and vibe, I highly recommend our **{matched_drink['name']}**! 
        It is crafted to be exceptionally *{matched_drink['vibe']}*. Would you like to customize it to fit your exact style?"
        """)

# --- FEATURE 4: DYNAMIC CONTEXTUAL DRINK CUSTOMIZATION ---
with col2:
    st.subheader("🎨 Customization Panel")
    if st.session_state.current_recommendation:
        drink = st.session_state.current_recommendation
        st.markdown(f"### Customizing: **{drink['name']}**")
        
        # Selection tools pulling criteria directly from selected item values
        chosen_size = st.selectbox("Select Size:", drink["sizes"])
        chosen_milk = st.selectbox("Select Milk Alternative:", drink["milks"])
        chosen_syrup = st.selectbox("Select Flavor Additions:", drink["syrups"])
        extra_shot = st.checkbox("Add Extra Espresso Shot? ☕")
        
        c1, c2 = st.columns(2)
        
        with c1:
            # Action button for Favorites List allocation
            if st.button("⭐ Save to Favorites"):
                if drink["name"] not in st.session_state.favorites:
                    st.session_state.favorites.append(drink["name"])
                    st.success(f"Added {drink['name']} to your saved checklist!")
                else:
                    st.info("This beverage is already in your favorites!")
                    
        with c2:
            # Action button tracking order transactions
            if st.button("🛒 Place Order"):
                order_details = {
                    "item": drink["name"],
                    "size": chosen_size,
                    "milk": chosen_milk,
                    "syrups": chosen_syrup,
                    "extra": "+1 Espresso Shot" if extra_shot else "Standard Strength"
                }
                st.session_state.order_history.append(order_details)
                
                # Verbal confirmation verifying acknowledgment of custom options parameters
                st.success(f"Order Placed! BaristaPulse is crafting your custom {chosen_size} {drink['name']} with {chosen_milk} and {chosen_syrup} flavor infusions.")
                st.rerun()
    else:
        st.info("Input your mood descriptor pattern in the chat panel to unlock custom beverage controls.")
