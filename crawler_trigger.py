from crawler.topic_queue import add_topics
import re

def extract_keywords(query):

    words = re.findall(r"[A-Za-z]{4,}",query.lower())

    return list(set(words))

def expand_crawling(query):

    keywords = extract_keywords(query)

    related = []

    for k in keywords:

        related.append(k)
        related.append(k+" theory")
        related.append(k+" algorithm")
        related.append(k+" applications")

    topics = list(set(related))

    print("Crawler expanding topics:",topics)

    add_topics(topics)
