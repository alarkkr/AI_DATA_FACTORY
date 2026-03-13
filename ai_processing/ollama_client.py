import requests
import threading

OLLAMA_URL="http://localhost:11434/api/generate"
MODEL="deepseek-r1:8b"

# limit simultaneous LLM calls
LLM_CONCURRENCY=1

semaphore = threading.Semaphore(LLM_CONCURRENCY)

def generate(prompt):

    payload={
        "model":MODEL,
        "prompt":prompt,
        "stream":False
    }

    with semaphore:

        try:
            r=requests.post(OLLAMA_URL,json=payload,timeout=600)
            data=r.json()

            return data.get("response","")

        except Exception as e:

            print("LLM request failed:",e)

            return ""
