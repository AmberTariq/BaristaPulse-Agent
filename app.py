import streamlit as st

# 1. Structural Layout Rules
st.set_page_config(page_title="BaristaPulse", page_icon="☕", layout="wide")

# 2. Master Style Injection: Creates the exact "Bold Typography Theme" from the video
st.markdown("""
    <style>
    /* Import modern bold typography font */
    @import url('https://googleapis.com');
    
    /* Background and global typography settings */
    .stApp {
        background-color: #FFFDD0 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Bold Title Typography styling matching your video video */
    .bold-main-title {
        font-size: 3rem !important;
        font-weight: 800 !important;
        color: #4A2E1B !important;
        letter-spacing: -0.04em !important;
        margin-bottom: 2px !important;
    }
    
    /* Left column workspace wrapper with crisp bold borders */
    .left-workspace-box {
        background-color: #FFF8E7 !important;
        padding: 28px;
        border-radius: 20px !important;
        border: 3px solid #4A2E1B !important;
        box-shadow: 5px 5px 0px 0px #4A2E1B !important;
        margin-bottom: 25px;
    }
    
    /* Crisp bold coffee cards matching your template layout */
    .coffee-menu-card {
        background-color: #FFF8E7 !important;
        padding: 24px;
        border-radius: 18px !important;
        border: 3px solid #4A2E1B !important;
        box-shadow: 5px 5px 0px 0px #4A2E1B !important;
        margin-bottom: 22px;
    }
    
    /* Text layout overrides */
    h2, h3, p, span {
        color: #4A2E1B !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    .theme-vibe-tag {
        background-color: #4A2E1B !important;
        color: #FFFDD0 !important;
        padding: 5px 14px;
        border-radius: 30px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
        letter-spacing: 0.03em;
    }
    
    /* Custom interactive button styles from the video */
    .stButton>button {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        background-color: #FFF8E7 !important;
        color: #4A2E1B !important;
        border: 3px solid #4A2E1B !important;
        border-radius: 12px !important;
        box-shadow: 3px 3px 0px 0px #4A2A1B !important;
    }
    .stButton>button:hover {
        background-color: #4A2E1B !important;
        color: #FFFDD0 !important;
    }
    </style>
    """, unsafe_html=True)

# 3. Split Screen into Two columns 
col1, col2 = st.columns([1, 1.15], gap="large")

with col1:
    st.markdown('<div class="left-workspace-box">', unsafe_html=True)
    st.markdown('<p class="bold-main-title">☕ BaristaPulse</p>', unsafe_html=True)
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
    
    if "active_selection" not in st.session_state:
        st.session_state.active_selection = None
        
    vibe_input = st.text_input("How are you feeling right now?", placeholder="e.g., I need a bold boost...", key="main_chat_input")
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
    st.markdown("### ⚡ QUICK MOOD EXPRESS")
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
    st.write("Ceremonial grade Uji matcha delicately whisked with velvety steamed oat milk and a touch of wild wildflower honey.")
    if st.button("Select Matcha Formula", key="m_btn"):
        st.session_state.active_selection = "Matcha Latte"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)

    # --- CARD 2: NITRO COLD BREW ---
    st.markdown('<div class="coffee-menu-card">', unsafe_html=True)
    st.markdown('<h3>⚡ Nitro Cold Brew</h3>', unsafe_html=True)
    st.markdown('<div class="theme-vibe-tag">Vibe: strong, bold, and highly energetic</div>', unsafe_html=True)
    st.write("Single-origin Ethiopian beans steeped for 20 hours and infused with pure nitrogen for a cascading, velvet mouthfeel.")
    if st.button("Select Nitro Formula", key="n_btn"):
        st.session_state.active_selection = "Nitro Cold Brew"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)

    # --- CARD 3: VANILLA OAT MACCHIATO ---
    st.markdown('<div class="coffee-menu-card">', unsafe_html=True)
    st.markdown('<h3>🍂 Vanilla Oat Macchiato</h3>', unsafe_html=True)
    st.markdown('<div class="theme-vibe-tag">Vibe: sweet, warm, and comforting</div>', unsafe_html=True)
    st.write("Freshly pulled espresso shots layered carefully over steamed vanilla bean organic oat milk and finished with a dense caramel drizzle.")
    if st.button("Select Macchiato Formula", key="v_btn"):
        st.session_state.active_selection = "Vanilla Oat Macchiato"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)
