import ollama
import sys
from typing import Optional, List, Dict

class OllamaClient:
    def __init__(self, host: str = "http://localhost:11434"):
        """Initialize the Ollama client with the given host."""
        self.client = ollama
        self.host = host
        
    def list_models(self) -> List[Dict]:
        """List all available models."""
        try:
            models = self.client.list()
            return models.get('models', [])  # Return the raw models list
        except Exception as e:
            print(f"Error listing models: {str(e)}")
            return []

    def generate_response(self, model: str, prompt: str) -> Optional[str]:
        """Generate a response using the specified model."""
        try:
            response = self.client.generate(model=model, prompt=prompt)
            return response['response']
        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return None

    def chat(self, model: str):
        """Interactive chat with the model."""
        print(f"Starting chat with {model} (type '/bye' to quit)")
        while True:
            try:
                user_input = input("\nYou: ").strip()
                if user_input.lower() == '/bye':
                    break
                
                response = self.generate_response(model, user_input)
                if response:
                    print(f"\n{model}: {response}")
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                break
        
        print("\nChat ended")

def main():
    # Initialize client
    client = OllamaClient()
    
    # List available models
    print("Available models:")
    models = client.list_models()
    if models:
        for model in models:
            # Extract just the model name from the model info
            model_name = model.get('name', model.get('model', 'Unknown'))
            print(f"- {model_name}")
    else:
        print("No models found or unable to fetch models")
        sys.exit(1)
    
    # Start chat with the first available model
    if models:
        default_model = models[0].get('name', models[0].get('model', 'Unknown'))
        print(f"\nStarting chat with {default_model}")
        client.chat(default_model)

if __name__ == "__main__":
    main() 