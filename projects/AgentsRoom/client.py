import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Load environment variables from a .env file
load_dotenv()

# Retrieve your API key from environment variables
api_key = os.getenv("API_KEY") 

# Initialize the OpenAI chat completion client with configuration
model_client = OpenAIChatCompletionClient(
    model="your_model_name",           # Specify the model name to use
    base_url="your_api_base_url",      # Specify the API base URL if different from default
    api_key=api_key,                   # Your OpenAI API key
    model_info={                      # Additional model configuration information
        "family": "qwen",             # Model family name
        "context_length": 12000,      # Maximum context length (tokens)
        "max_output_tokens": 8192,    # Maximum tokens in model output
        "tool_choice_supported": True,  # Whether the model supports tool choice
        "tool_choice_required": False,   # Whether tool choice is mandatory
        "structured_output": True,       # Whether the model outputs structured data (e.g., JSON)
        "vision": False,                 # Whether the model supports vision inputs
        "function_calling": False,       # Whether function calling is enabled
        "json_output": True              # Whether output is JSON formatted
    }
)
