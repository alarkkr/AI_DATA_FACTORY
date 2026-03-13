import re

def clean_topic(topic):

    topic=topic.lower().strip()

    words=re.findall(r"[a-z]{4,}",topic)

    if len(words)==0:
        return None

    topic=" ".join(words)

    return topic
