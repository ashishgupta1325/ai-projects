# Ollama Client

A simple Python client for interacting with Ollama models.

## Prerequisites

1. Make sure you have [Ollama](https://ollama.ai/) installed and running on your system
2. Python 3.7 or higher

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure Ollama is running on your system (default port: 11434)

## Usage

Run the script:
```bash
python ollama_client.py
```

The script will:
1. List all available models in your Ollama installation
2. Start an interactive chat session with the first available model
3. You can type 'exit' to quit the chat

## Features

- List available models
- Interactive chat interface
- Error handling for common issues
- Configurable host address

## Example Usage in Code

```python
from ollama_client import OllamaClient

client = OllamaClient()
models = client.list_models()
response = client.generate_response("llama2", "Tell me a joke")
print(response)
```
