import re

def extract_topics(query):

    words = re.findall(r"[A-Za-z]{4,}",query.lower())

    return list(set(words))
