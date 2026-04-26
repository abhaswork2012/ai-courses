# Create a CodeAgent with DuckDuckGo search capability
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")  # Replace with your actual model ID
)