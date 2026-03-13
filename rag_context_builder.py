from database.vector_search import search

def build_context(query):

    results = search(query, k=5)

    context = "\n".join(results)

    return context
