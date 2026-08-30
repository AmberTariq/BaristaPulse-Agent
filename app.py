import streamlit as st

# Set up page configurations with a friendly coffee emoji
st.set_page_config(page_title="BaristaPulse AI", page_icon="☕", layout="wide")

# Injecting the "Bold Typography Theme" styles directly
st.markdown("""
    <style>
    /* Main body typography and color space */
    @import url('https://googleapis.com');
    
    .stApp {
        background-color: #FFFDD0;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Main Headings Styling */
    h1 {
        font-size: 2.85rem !important;
        font-weight: 800 !important;
        color: #4A2E1B !important;
        letter-spacing: -0.03em;
        margin-bottom: 5px !important;
    }
    
    h2, h3 {
        font-weight: 700 !important;
        color: #4A2E1B !important;
        letter-spacing: -0.01em;
    }
    
    /* Left column workspace wrapper container */
    .left-workspace-box {
        background-color: #FFF8E7;
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #4A2E1B;
        box-shadow: 4px 4px 0px 0px #4A2E1B;
        margin-bottom: 25px;
    }
    
    /* Luxury Premium Coffee Menu Cards */
    .coffee-menu-card {
        background-color: #FFF8E7;
        padding: 24px;
        border-radius: 18px;
        border: 2px solid #4A2E1B;
        box-shadow: 4px 4px 0px 0px #4A2E1B;
        margin-bottom: 22px;
    }
    
    /* Custom Badge for Coffee Vibe Profiles */
    .theme-vibe-tag {
        background-color: #4A2E1B;
        color: #FFFDD0 !important;
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Style descriptions text */
    .drink-description-text {
        font-size: 1.05rem;
        color: #5D4037;
        line-height: 1.5;
        margin-bottom: 10px;
    }
    
    /* Quick Mood Express Buttons styling overlay */
    .stButton>button {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        background-color: #FFF8E7 !important;
        color: #4A2E1B !important;
        border: 2px solid #4A2E1B !important;
        border-radius: 12px !important;
        box-shadow: 2px 2px 0px 0px #4A2E1B !important;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #4A2E1B !important;
        color: #FFFDD0 !important;
        box-shadow: 0px 0px 0px 0px #4A2E1B !important;
        transform: translate(2px, 2px);
    }
    </style>
    """, unsafe_html=True)

# 2. Main Layout Structure Split Configuration
col1, col2 = st.columns([1, 1.15], gap="large")

with col1:
    st.markdown('<div class="left-workspace-box">', unsafe_html=True)
    st.markdown("<h1>☕ BaristaPulse</h1>", unsafe_html=True)
    st.caption("Welcome to The Coffee Logic — Your Personal AI Companion")
    
    st.markdown("""
    ### Hey there and welcome to BaristaPulse! 👋
    I am **BaristaPulse**, your personal cafe companion. I'm here to recommend the ultimate handcrafted cup tailored to your exact mood, energy, or current feeling.
    
    Our cafe proudly curates 3 signature drinks with distinct vibes:
    * 🌿 **Matcha Latte** (vibe: creamy, smooth, and earthy)
    * ⚡ **Nitro Cold Brew** (vibe: strong, bold, and highly energetic)
    * ✨ **Vanilla Oat Macchiato** (vibe: sweet, warm, and comforting)
    
    How are you feeling right now? Tell me your vibe or pick a mood below to get started! 👇
    """)
    st.markdown('</div>', unsafe_html=True)
    
    # Initialize interactive state values
    if "active_selection" not in st.session_state:
        st.session_state.active_selection = None
        
    vibe_input = st.text_input("How are you feeling right now?", placeholder="e.g., I need a bold boost or something calming...", key="main_chat_input")
    if vibe_input:
        if any(w in vibe_input.lower() for w in ["bold", "energy", "strong"]):
            st.session_state.active_selection = "Nitro Cold Brew"
        elif any(w in vibe_input.lower() for w in ["calm", "relax", "earthy"]):
            st.session_state.active_selection = "Matcha Latte"
        elif any(w in vibe_input.lower() for w in ["sweet", "warm", "comfort"]):
            st.session_state.active_selection = "Vanilla Oat Macchiato"

    if st.session_state.active_selection:
        st.success(f"🌟 **BaristaPulse:** 'Hey there! Based on your preference, I highly recommend our **{st.session_state.active_selection}**!'")

    st.write("---")
    st.markdown("### ⚡ QUICK MOOD EXPRESS", unsafe_html=True)
    if st.button("🔥 High Energy Boost (Nitro Cold Brew)"):
        st.session_state.active_selection = "Nitro Cold Brew"
        st.rerun()
    if st.button("🧸 Cozy & Sweet Comfort (Vanilla Oat Macchiato)"):
        st.session_state.active_selection = "Vanilla Oat Macchiato"
        st.rerun()
    if st.button("🌿 Serene Earthy Zen (Matcha Latte)"):
        st.session_state.active_selection = "Matcha Latte"
        st.rerun()

with col2:
    st.markdown("<h2>📋 DAILY SIGNATURE MENU</h2>", unsafe_html=True)
    
    # --- CARD 1: MATCHA LATTE ---
    st.markdown('<div class="coffee-menu-card">', unsafe_html=True)
    st.markdown('<h3>🌿 Matcha Latte</h3>', unsafe_html=True)
    st.markdown('<div class="theme-vibe-tag">Vibe: creamy, smooth, and earthy</div>', unsafe_html=True)
    st.markdown('<p class="drink-description-text">Ceremonial grade Uji matcha delicately whisked with velvety steamed oat milk and a touch of wild wildflower honey.</p>', unsafe_html=True)
    st.caption("✨ Earthy Umami | 🥛 Silky Creamy Milk | 🍯 Mild Sweetness")
    if st.button("Select Matcha Formula", key="m_btn"):
        st.session_state.active_selection = "Matcha Latte"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)

    # --- CARD 2: NITRO COLD BREW ---
    st.markdown('<div class="coffee-menu-card">', unsafe_html=True)
    st.markdown('<h3>⚡ Nitro Cold Brew</h3>', unsafe_html=True)
    st.markdown('<div class="theme-vibe-tag">Vibe: strong, bold, and highly energetic</div>', unsafe_html=True)
    st.markdown('<p class="drink-description-text">Single-origin Ethiopian beans steeped for 20 hours and infused with pure nitrogen for a cascading, velvet mouthfeel.</p>', unsafe_html=True)
    st.caption("💥 High Caffeine | 🍇 Berry Undertones | 🍫 Cocoa Finish")
    if st.button("Select Nitro Formula", key="n_btn"):
        st.session_state.active_selection = "Nitro Cold Brew"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)

    # --- CARD 3: VANILLA OAT MACCHIATO ---
    st.markdown('<div class="coffee-menu-card">', unsafe_html=True)
    st.markdown('<h3>🍂 Vanilla Oat Macchiato</h3>', unsafe_html=True)
    st.markdown('<div class="theme-vibe-tag">Vibe: sweet, warm, and comforting</div>', unsafe_html=True)
    st.markdown('<p class="drink-description-text">Freshly pulled espresso shots layered carefully over steamed vanilla bean organic oat milk and finished with a dense caramel drizzle.</p>', unsafe_html=True)
    st.caption("🍂 Warm Vanilla Bean | ☕ Roasted Espresso | 🍯 Golden Caramel")
    if st.button("Select Macchiato Formula", key="v_btn"):
        st.session_state.active_selection = "Vanilla Oat Macchiato"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)
