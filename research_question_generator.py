from ai_processing.ollama_client import generate

def generate_questions(topic):

    prompt = f"""
Generate 5 research questions about:

{topic}

Return them as short sentences.
"""

    response = generate(prompt)

    return response
