import json
import time

FILE = "reasoning_memory.jsonl"

def store_reasoning(query,result):

    record = {
        "time": time.time(),
        "query": query,
        "answer": result.get("answer","")
    }

    with open(FILE,"a",encoding="utf-8") as f:
        f.write(json.dumps(record)+"\n")
