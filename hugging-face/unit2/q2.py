from smolagents import CodeAgent, ToolCallingAgent,DuckDuckGoSearchTool,VisitWebpageTool, HfApiModel

# Create web agent and manager agent structure
web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), VisitWebpageTool()], 
    model=HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct"),
    max_steps=10,
    name="search", 
    description="Agent to perform web searches and visit webpages."
)

manager_agent = CodeAgent(model=HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct"),
    managed_agents=[web_agent],
    additional_authorized_imports=["pandas", "time", "numpy"])