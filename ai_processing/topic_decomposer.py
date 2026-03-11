def decompose(text):

    topics = {}

    words = text.split()

    topics["summary"] = " ".join(words[:200])

    return topics
