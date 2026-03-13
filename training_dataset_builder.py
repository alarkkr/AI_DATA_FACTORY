import json
import re

INPUT="knowledge_store.jsonl"
OUTPUT="llm_training_dataset.jsonl"

def clean_topic(topic):

    topic=topic.strip().lower()

    if len(topic)<3:
        return None

    if topic in ["summary","article","page","introduction"]:
        return None

    return topic

def build():

    seen=set()

    samples=[]

    with open(INPUT,"r",encoding="utf-8") as f:

        for line in f:

            record=json.loads(line)

            topic=clean_topic(record.get("topic",""))

            text=record.get("content","")

            if topic is None:
                continue

            if len(text)<200:
                continue

            key=topic+text[:100]

            if key in seen:
                continue

            seen.add(key)

            sample={
                "prompt":f"Explain {topic}",
                "response":text
            }

            samples.append(sample)

    with open(OUTPUT,"w",encoding="utf-8") as f:

        for s in samples:
            f.write(json.dumps(s)+"\n")

    print("Clean dataset samples:",len(samples))
