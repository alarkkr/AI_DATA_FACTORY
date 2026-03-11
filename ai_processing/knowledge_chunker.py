def chunk_knowledge(topics):

    chunks = []

    for t in topics:

        chunk = {
            "topic": t,
            "content": topics[t]
        }

        chunks.append(chunk)

    return chunks
