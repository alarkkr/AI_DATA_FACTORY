from database.vector_search import search

def coverage_score(query):

    results = search(query, k=3)

    total = 0

    for r in results:
        total += len(r)

    return total
