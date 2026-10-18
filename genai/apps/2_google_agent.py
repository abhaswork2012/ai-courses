from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq

model = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()

agent = create_agent(
    model=model,
    tools=[search.run],
    system_prompt="You are a agent that can answer questions using Google search results. Use the search tool to find information and provide accurate answers.")

while True:
    query = input("Enter your question (or 'quit' to quit): ")
    if query.lower() == 'quit':
        print("Goodbye")
        break
    response = agent.invoke({"messages": [{"role": "user", "content": query}]})
    print(response["messages"][-1].content)