def build_prompt(question,context):

    prompt = f"""
You are an AI assistant.

Answer the question using ONLY the provided knowledge.

Knowledge:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    return prompt
