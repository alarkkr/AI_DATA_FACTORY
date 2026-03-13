import json
import time

FILE = "research_memory.jsonl"

def store_insight(topic, insight):

    record = {
        "time": time.time(),
        "topic": topic,
        "insight": insight
    }

    with open(FILE,"a",encoding="utf-8") as f:
        f.write(json.dumps(record)+"\n")

    print("Research insight stored:",topic)
