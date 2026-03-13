from rag_context_builder import build_context
from ai_processing.ollama_client import generate

def reason_with_llm(query):

    context = build_context(query)

    prompt = f"""
You are an AI research assistant.

Use the knowledge below to answer the question.

Knowledge:
{context}

Question:
{query}

Explain clearly.
"""

    answer = generate(prompt)

    result = {
        "query": query,
        "answer": answer,
        "context_size": len(context)
    }

    return result
