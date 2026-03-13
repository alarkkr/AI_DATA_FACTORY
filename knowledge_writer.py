import json
from domain_filter import allowed

STORE="knowledge_store.jsonl"

def store_new_knowledge(topic,text):

    if not allowed(topic):
        return

    record={
        "topic":topic,
        "content":text
    }

    with open(STORE,"a",encoding="utf-8") as f:
        f.write(json.dumps(record)+"\n")
