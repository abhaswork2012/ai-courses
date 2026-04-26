# Set up secure code execution environment

from smolagents import CodeAgent, HfApiModel
from smolagents.sandbox import E2BSandbox

agent = CodeAgent(
    tools=[],
    model=HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct"),
    # Add security configuration
    sandbox=E2BSandbox(),
)