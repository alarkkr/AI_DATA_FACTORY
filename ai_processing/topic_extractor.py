import re

def extract_topics(text):

    words = re.findall(r"\b[A-Z][a-zA-Z]{4,}\b",text)

    topics = list(set(words))

    return topics[:10]
