import streamlit as st

# 1. Page Title and Header Setup
st.title("☕ BaristaPulse: Your Aesthetic Coffee Agent ✨")
st.write("Welcome! I am **BaristaPulse**, your personal coffee matchmaker. Tell me your mood or preference below!")
st.write("---")

# 2. Split Screen into Two Beautiful Columns (Left for Chat & Info, Right for Menu)
col1, col2 = st.columns([1, 1.2])

with col1:
    st.header("💬 Conversation & Profile Workspace")
    
    # Text entry bar for mood analysis
    vibe_input = st.text_input("How are you feeling right now?", placeholder="e.g., I need a bold energetic boost or something calming...")
    
    # Setup simple button state memory
    if "clicked_drink" not in st.session_state:
        st.session_state.clicked_drink = None

    # Handle text matching logic
    if vibe_input:
        if "bold" in vibe_input.lower() or "energy" in vibe_input.lower() or "strong" in vibe_input.lower():
            st.session_state.clicked_drink = "Nitro Cold Brew"
        elif "calm" in vibe_input.lower() or "relax" in vibe_input.lower() or "earthy" in vibe_input.lower():
            st.session_state.clicked_drink = "Matcha Latte"
        elif "sweet" in vibe_input.lower() or "warm" in vibe_input.lower() or "comfort" in vibe_input.lower():
            st.session_state.clicked_drink = "Vanilla Oat Macchiato"

    # Display BaristaPulse's active response message block
    if st.session_state.clicked_drink:
        st.success(f"🌟 **BaristaPulse:** 'Hey there! Based on your preference, I highly recommend our **{st.session_state.clicked_drink}**! Let me know if you would like to order it!'")
    else:
        st.info("💡 Type your current mood profile in the input bar or click a 'Daily Menu' choice on the right to kick off your customization logic!")

    st.write("---")
    st.subheader("⚡ QUICK MOOD EXPRESS")
    if st.button("🔥 High Energy Boost (Nitro Cold Brew)"):
        st.session_state.clicked_drink = "Nitro Cold Brew"
    if st.button("🧸 Cozy & Sweet Comfort (Vanilla Oat Macchiato)"):
        st.session_state.clicked_drink = "Vanilla Oat Macchiato"
    if st.button("🌿 Serene Earthy Zen (Matcha Latte)"):
        st.session_state.clicked_drink = "Matcha Latte"

with col2:
    st.header("📋 DAILY SIGNATURE MENU")
    
    # --- CARD 1: MATCHA LATTE ---
    with st.expander("🌿 Matcha Latte — 'creamy, smooth, and earthy'", expanded=True):
        st.write("Ceremonial grade Uji matcha delicately whisked with velvety steamed oat milk and a touch of wild wildflower honey.")
        st.caption("✨ Earthy Umami | 🥛 Silky Creamy Milk | 🍯 Mild Sweetness")
        if st.button("Select Matcha Formula", key="matcha_btn"):
            st.session_state.clicked_drink = "Matcha Latte"
            st.rerun()

    # --- CARD 2: NITRO COLD BREW ---
    with st.expander("⚡ Nitro Cold Brew — 'strong, bold, and energetic'", expanded=True):
        st.write("Single-origin Ethiopian beans steeped for 20 hours and infused with pure nitrogen for a cascading, velvet mouthfeel.")
        st.caption("💥 High Caffeine | 🍇 Berry Undertones | 🍫 Cocoa Finish")
        if st.button("Select Nitro Formula", key="nitro_btn"):
            st.session_state.clicked_drink = "Nitro Cold Brew"
            st.rerun()

    # --- CARD 3: VANILLA OAT MACCHIATO ---
    with st.expander("🍂 Vanilla Oat Macchiato — 'sweet, warm, and comforting'", expanded=True):
        st.write("Freshly pulled espresso shots layered carefully over steamed vanilla bean organic oat milk and a dense caramel drizzle.")
        st.caption("🍂 Warm Vanilla Bean | ☕ Roasted Espresso | 🍯 Golden Caramel")
        if st.button("Select Macchiato Formula", key="macchiato_btn"):
            st.session_state.clicked_drink = "Vanilla Oat Macchiato"
            st.rerun()
