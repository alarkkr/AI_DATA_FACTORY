import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def ask_llm(prompt):

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(OLLAMA_URL,json=payload)

    data = r.json()

    return data["response"]
