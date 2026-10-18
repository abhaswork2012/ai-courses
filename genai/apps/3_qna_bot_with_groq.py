from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st

llm = ChatGroq(model="openai/gpt-oss-20b",streaming=True)
search = GoogleSerperAPIWrapper()
tools = [search.run]

if 'memory' not in st.session_state:
    st.session_state.memory = MemorySaver()
    st.session_state.history = []

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a agent that can answer questions using Google search results. Use the search tool to find information and provide accurate answers.",
    checkpointer=st.session_state.memory)

###Building Web Interface
st.subheader("Quick Answer")

for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask anything?")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role": "user", "content": query})
    response = agent.stream({"messages": [{"role": "user", "content": query}]}, {"configurable": {"thread_id": 1}},stream_mode='messages')
    ai_container = st.chat_message("ai")
    with ai_container:
        space = st.empty()  
        msg = ""
        for chunk in response:
            msg += chunk[0].content
            space.write(msg)
        
        
        st.session_state.history.append({"role": "ai", "content": msg})
            