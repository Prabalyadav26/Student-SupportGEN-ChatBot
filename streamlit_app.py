import streamlit as st
import time

# Importing your backend logic
# Ensure your backend code is saved as 'chatbot.py' in the same directory
from chatbot import ask_chatbot

# ---------------- PAGE CONFIGURATION ---------------- #
st.set_page_config(
    page_title="Intelligent Support AI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>
    /* Global container padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 850px;
    }
    
    /* Header styling with gradient */
    .main-header {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    
    /* Subtitle styling */
    .sub-header {
        text-align: center;
        font-size: 1.1rem;
        color: #6B7280;
        margin-top: -5px;
        margin-bottom: 40px;
        font-weight: 500;
    }
    
    /* Tech stack badges in the sidebar */
    .tech-badge {
        display: inline-block;
        padding: 4px 10px;
        background: #F1F5F9;
        color: #334155;
        border: 1px solid #CBD5E1;
        border-radius: 15px;
        font-size: 12px;
        font-weight: 600;
        margin: 2px;
    }

    /* System messages (greetings/thanks) styling */
    .system-msg {
        color: #059669;
        font-weight: 600;
        padding: 10px;
        border-left: 4px solid #10B981;
        background-color: #ECFDF5;
        border-radius: 4px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE MANAGEMENT ---------------- #
# Initialize chat history array
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR NAVIGATION & SETTINGS ---------------- #
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712010.png", width=60)
    st.markdown("## System Dashboard")
    
    st.markdown("### 🛠️ Architecture")
    st.markdown("""
        <div style='margin-bottom: 15px;'>
            <span class='tech-badge'>Groq LLM</span>
            <span class='tech-badge'>FAISS Vector DB</span>
            <span class='tech-badge'>Custom NLP</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.info(
        "This assistant uses intention detection to handle greetings, "
        "and relies on vector search and GenAI for complex queries."
    )
    
    st.divider()
    
    st.markdown("### ⚙️ Session Controls")
    if st.button("🗑️ Clear Chat History", use_container_width=True, type="secondary"):
        st.session_state.messages = []
        st.rerun()
        
    st.divider()
    st.caption("Developed with ❤️ | Streamlit")

# ---------------- MAIN HEADER ---------------- #
st.markdown("<div class='main-header'>Intelligent Support AI</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-header'>Powered by Groq & Semantic Search</div>",
    unsafe_allow_html=True
)

# ---------------- DISPLAY CHAT HISTORY ---------------- #
# Iterate through the session state and render previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- CHAT INPUT & PROCESSING ---------------- #
prompt = st.chat_input("Ask me anything...")

if prompt:
    # 1. Display and store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Display assistant response with loading spinner
    with st.chat_message("assistant"):
        with st.spinner("🧠 Processing query..."):
            time.sleep(0.3) # Smooth UI transition
            
            try:
                # Call your backend logic here
                response = ask_chatbot(prompt)
                
                # Highlight system intent messages (like "Hello" or "Thanks")
                if response in ["Hello! 👋 How can I help you today?", "You're welcome! 😊"]:
                    st.markdown(f"<div class='system-msg'>{response}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(response)
                    
            except Exception as e:
                # Fallback error handling so the UI doesn't crash completely
                response = f"⚠️ **Backend Error:**\n\n`{str(e)}`\n\nPlease check your vector store or Groq API connection."
                st.error(response)

    # 3. Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})