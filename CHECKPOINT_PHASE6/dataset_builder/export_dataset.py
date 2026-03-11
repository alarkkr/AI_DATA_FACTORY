import json

INPUT="knowledge_store.jsonl"
OUTPUT="training_dataset.jsonl"

def export_dataset():

    with open(INPUT,"r") as f:

        records=[json.loads(l) for l in f]

    with open(OUTPUT,"w") as f:

        for r in records:

            sample={
                "input":r["topic"],
                "output":r["content"]
            }

            f.write(json.dumps(sample)+"\n")

    print("Dataset exported")
