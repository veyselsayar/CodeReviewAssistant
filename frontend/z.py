import requests
from ollama import chat


def check_ollama_service():
    """Check if the Ollama service is running and responsive."""
    try:
        response = requests.get("http://127.0.0.1:11435")
        if response.status_code == 200:
            print("Ollama service is running and responsive.")
        else:
            print(f"Ollama service returned unexpected status: {response.status_code}")
    except Exception as e:
        print(f"Failed to connect to the Ollama service: {e}")
        raise ConnectionError("Ollama service is not responsive.")


try:
    # Check if the Ollama service is running
    check_ollama_service()

    # Attempt to use the Ollama chat client
    response = chat("Hello, how can I help you?")
    print("Response from Ollama:", response)

except ConnectionError as ce:
    print(f"Connection error: {ce}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
