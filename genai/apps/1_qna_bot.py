from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')
st.title("AI QnA Bot")
st.markdown("QnA bot with Langchain and Google Gemini!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything?")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})
    response = llm.invoke(query)
    st.chat_message("ai").markdown(response.content)
    st.session_state.messages.append({"role": "ai", "content": response.content})