import streamlit as st

# 1. Structural layout rules with premium dark theme parameters
st.set_page_config(page_title="BaristaPulse", page_icon="☕", layout="wide")

# Custom CSS for the luxury dark-roast coffee shop theme
st.markdown("""
    <style>
    .stApp {
        background-color: #121214;
    }
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #F4EAE1 !important;
    }
    /* Style for the Left Sidebar / Profile Column */
    .chat-container {
        background-color: #1A1A1E;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #2A2A30;
    }
    /* Style for Menu Item Cards */
    .menu-card {
        background-color: #1A1A1E;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #2A2A30;
        margin-bottom: 16px;
    }
    .vibe-badge {
        background-color: #2D2621;
        color: #DDA15E !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 12px;
    }
    /* Custom buttons styled as Ask Barista actions */
    .stButton>button {
        background-color: #DDA15E !important;
        color: #121214 !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100%;
    }
    </style>
    """, unsafe_html=True)

# 2. Main Layout Split (Left Workspace vs. Right Interactive Menu Grid)
left_col, right_col = st.columns([1, 1.2])

with left_col:
    st.markdown('<div class="chat-container">', unsafe_html=True)
    st.image("https://icons8.com", width=70) # Logo placeholder
    st.title("☕ BaristaPulse")
    st.caption("Welcome to The Coffee Logic — Your Personal AI Assistant")
    
    st.markdown("""
    ### Hey there and welcome to BaristaPulse! 👋
    I am **BaristaPulse**, your personal cafe companion. I'm here to recommend the ultimate handcrafted cup tailored to your exact mood, energy, or current feeling.
    
    Our cafe proudly curates 3 signature drinks with distinct vibes:
    * 🌿 **Matcha Latte** (vibe: creamy, smooth, and earthy)
    * ⚡ **Nitro Cold Brew** (vibe: strong, bold, and highly energetic)
    * ✨ **Vanilla Oat Macchiato** (vibe: sweet, warm, and comforting)
    
    How are you feeling right now? Tell me your vibe or pick a mood below to get started! 👇
    """)
    
    # Session handler for capturing interactive choices
    if "selected_vibe" not in st.session_state:
        st.session_state.selected_vibe = "None Selected Yet"
    
    st.write("---")
    st.subheader("⚡ QUICK MOOD EXPRESS")
    
    # Grid of quick-express buttons matching the bottom selector row
    m1, m2 = st.columns(2)
    with m1:
        if st.button("🔥 Need High Energy"):
            st.session_state.selected_vibe = "Nitro Cold Brew"
    with m2:
        if st.button("🧸 Cozy & Sweet Comfort"):
            st.session_state.selected_vibe = "Vanilla Oat Macchiato"
            
    m3, m4 = st.columns(2)
    with m3:
        if st.button("🌿 Serene & Earthy Zen"):
            st.session_state.selected_vibe = "Matcha Latte"
    with m4:
        if st.button("✨ Reset Selection"):
            st.session_state.selected_vibe = "None Selected Yet"
            
    st.write("---")
    st.info(f"🔮 **BaristaPulse Active Target Action:** {st.session_state.selected_vibe}")
    st.markdown('</div>', unsafe_html=True)

with right_col:
    st.markdown("### 📋 DAILY SPECIALS | Signature Menu")
    
    # --- CARD 1: MATCHA LATTE ---
    st.markdown('<div class="menu-card">', unsafe_html=True)
    st.markdown('<h3>🌿 Matcha Latte</h3>', unsafe_html=True)
    st.markdown('<span class="vibe-badge">VIBE PROFILE: "creamy, smooth, and earthy"</span>', unsafe_html=True)
    st.write("Ceremonial grade Uji matcha delicately whisked with velvety steamed oat milk and a touch of wild wildflower honey sweetener.")
    st.caption("✨ Earthy Umami | 🥛 Silky Creamy Milk | 🍯 Mild Sweetness")
    if st.button("Ask Barista for Matcha Formula", key="ask_matcha"):
        st.session_state.selected_vibe = "Matcha Latte"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)

    # --- CARD 2: NITRO COLD BREW ---
    st.markdown('<div class="menu-card">', unsafe_html=True)
    st.markdown('<h3>⚡ Nitro Cold Brew</h3>', unsafe_html=True)
    st.markdown('<span class="vibe-badge">VIBE PROFILE: "strong, bold, and highly energetic"</span>', unsafe_html=True)
    st.write("Single-origin Ethiopian beans steeped for 20 hours and infused with pure nitrogen for a cascading, creamy head and velvet mouthfeel.")
    st.caption("💥 High Caffeine | 🍇 Berry Undertones | 🍫 Cocoa Finish")
    if st.button("Ask Barista for Nitro Formula", key="ask_nitro"):
        st.session_state.selected_vibe = "Nitro Cold Brew"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)

    # --- CARD 3: VANILLA OAT MACCHIATO ---
    st.markdown('<div class="menu-card">', unsafe_html=True)
    st.markdown('<h3>✨ Vanilla Oat Macchiato</h3>', unsafe_html=True)
    st.markdown('<span class="vibe-badge">VIBE PROFILE: "sweet, warm, and comforting"</span>', unsafe_html=True)
    st.write("Freshly pulled espresso shots layered carefully over steamed vanilla bean organic oat milk and finished with a dense caramel crosshatch drizzle.")
    st.caption("🍂 Warm Vanilla Bean | ☕ Roasted Espresso | 🍯 Golden Caramel")
    if st.button("Ask Barista for Macchiato Formula", key="ask_macchiato"):
        st.session_state.selected_vibe = "Vanilla Oat Macchiato"
        st.rerun()
    st.markdown('</div>', unsafe_html=True)
