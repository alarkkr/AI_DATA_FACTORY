import json

FILE="llm_training_dataset.jsonl"

count=0

with open(FILE,"r",encoding="utf-8") as f:
    for line in f:
        count+=1

print("\nTraining dataset samples:",count)
