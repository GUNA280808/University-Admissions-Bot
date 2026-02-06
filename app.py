import streamlit as st
from chatbot import AdmissionsChatbot

bot = AdmissionsChatbot("knowledge_base.json")

st.set_page_config(page_title="Smart Admissions Assistant", page_icon="🎓", layout="centered")

# Custom styling
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #e3f2fd, #fce4ec);
}
.chat-box {
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
}
.user {
    background-color: #d1e7dd;
}
.bot {
    background-color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓  University Admissions Assistant")
st.caption("Ask about programs, fees, careers, deadlines, and more.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role_class = "user" if msg["role"] == "user" else "bot"
    st.markdown(
        f"<div class='chat-box {role_class}'><b>{msg['role'].title()}:</b> {msg['content']}</div>",
        unsafe_allow_html=True
    )

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your question...")
    submit = st.form_submit_button("Send")

if submit and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = bot.get_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": response})
    st.rerun()
