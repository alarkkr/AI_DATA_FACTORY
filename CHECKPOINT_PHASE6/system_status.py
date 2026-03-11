import os

def check():

    print("\nSYSTEM STATUS\n")

    if os.path.exists("vector.index"):
        print("Vector DB: READY")

    if os.path.exists("knowledge_store.jsonl"):
        print("Knowledge Store: READY")

    if os.path.exists("knowledge_graph.json"):
        print("Knowledge Graph: READY")

    if os.path.exists("topics.txt"):
        print("Topic Queue: ACTIVE")

check()
