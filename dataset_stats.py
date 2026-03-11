import json

file="knowledge_store.jsonl"

count=0

topics=set()

with open(file,"r",encoding="utf-8") as f:

    for line in f:

        d=json.loads(line)

        count+=1

        topics.add(d["topic"])

print("\nDATASET STATS\n")

print("Total knowledge chunks:",count)

print("Unique topics:",len(topics))
