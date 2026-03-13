import os

DATASET="llm_training_dataset.jsonl"

MIN_SAMPLES=1000

def ready():

    if not os.path.exists(DATASET):
        return False

    with open(DATASET,"r") as f:
        count=sum(1 for _ in f)

    return count>=MIN_SAMPLES
