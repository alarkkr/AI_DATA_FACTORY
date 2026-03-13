from ai_processing.ollama_client import generate

def generate_hypothesis(topic):

    prompt=f"""
You are an AI research scientist.

Generate a short research hypothesis about the topic:

{topic}

Return 2-3 sentences.
"""

    response=generate(prompt)

    return response
