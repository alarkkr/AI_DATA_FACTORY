from rag_context_builder import build_context
import re

def reason(query):

    context = build_context(query)

    sentences = re.split(r"[.!?]", context)

    key_points = sentences[:5]

    reasoning = {
        "query": query,
        "context_size": len(context),
        "insights": key_points
    }

    return reasoning
