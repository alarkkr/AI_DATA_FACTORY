import json

STORE = "knowledge_store.jsonl"

def detect_gaps():

    topics = {}

    with open(STORE,"r",encoding="utf-8") as f:

        for line in f:

            data = json.loads(line)

            topic = data["topic"]

            topics[topic] = topics.get(topic,0) + 1

    gaps = []

    for t,count in topics.items():

        if count < 5:

            gaps.append(t)

    return gaps
