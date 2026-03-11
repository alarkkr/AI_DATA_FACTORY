def build_context(docs):

    context = ""

    for i,d in enumerate(docs):

        context += f"[Document {i+1}]\n"

        context += d + "\n\n"

    return context
