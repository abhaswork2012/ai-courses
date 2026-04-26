from smolagents import HfApiModel, LiteLLMModel

# Initialize Hugging Face model
hf_model = HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct")

# Initialize LiteLLM model as an alternative model
other_model = LiteLLMModel(model_id="anthropic/claude-3-sonnet")

# Set the model to hf_model or alternative model
model = hf_model  # Alternatively, you can switch this to `other_model`