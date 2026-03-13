from ai_processing.ollama_client import generate

def generate_hypothesis(topic):

    prompt = f"""
You are an AI researcher.

Generate a scientific hypothesis related to:

{topic}

Explain briefly.
"""

    result = generate(prompt)

    return result
