# BaristaPulse: Your Aesthetic Coffee Agent ☕✨

**BaristaPulse** is an interactive, customer-facing AI agent interface designed to match a user's current mood or specific cravings with the perfect premium coffee selection. 

Built using **Python** and the **Streamlit** web framework, the application connects a modern user experience with back-end artificial intelligence powered by **Google's Gemini API**. The agent dynamically interprets informal user inputs (e.g., *"I'm feeling tired, I need something energetic"*) to generate highly curated, context-aware coffee recommendations in real-time.

---

## 🚀 Key Features

* **Instant Mood-to-Coffee Matching**: Enter how you feel or what you crave, and the agent serves up a tailored beverage recommendation.
* **Context-Aware Recommendations**: Powered by Gemini to understand slang, energy levels, and descriptive flavor preferences.
* **Aesthetic & Responsive Minimal UI**: A clean, dual-panel layout optimized for both desktop browsers and mobile screens.
* **Static Signature Menu**: Displays a quick glance of standard signature offerings alongside the dynamic AI workspace.

## 🛠️ Tech Stack

* **Frontend & Backend UI Framework**: Streamlit
* **Core Language**: Python
* **LLM Orchestration**: Google Gemini API (via Google AI Studio)
* **Deployment**: Streamlit Community Cloud

---

## 💻 Local Installation & Setup

Follow these simple steps to run BaristaPulse locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com
cd BaristaPulse
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Make sure you have a `requirements.txt` file setup, then run:
```bash
pip install -r requirements.txt
```
*(Your dependencies should include `streamlit` and `google-generativeai`)*

### 4. Configure Your API Key
To allow Streamlit to securely access your Gemini API key locally, create a local secrets file:
```bash
mkdir .streamlit
touch .streamlit/secrets.toml
```
Open `.streamlit/secrets.toml` and add your API key:
```toml
GEMINI_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
```

### 5. Run the Application
```bash
streamlit run app.py
```

---

## 🌐 Live Deployment

The application is globally accessible and deployed on Streamlit Community Cloud. 
👉 **[Try the Live App Here!](https://baristapulse-agent-bguggitkbnfb4iz5d5jwop.streamlit.app/)**

## 📄 License
This project is open-source and available under the **MIT License**.
