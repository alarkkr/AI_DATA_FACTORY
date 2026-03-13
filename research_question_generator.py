from ai_processing.ollama_client import generate

def generate_questions(topic):

    prompt=f"""
You are an AI research assistant.

Generate 3 research questions about:

{topic}
"""

    response=generate(prompt)

    return response
