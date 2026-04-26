# Create a tool-calling agent
from smolagents import ToolCallingAgent,DuckDuckGoSearchTool,HfApiModel

agent = ToolCallingAgent(
    # Add configuration here
    tools=[DuckDuckGoSearchTool()],  
    model=HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct"),  
    name="SearchAgent",  
    description="An agent that uses DuckDuckGo to search the web.",  
    max_steps=5,
)