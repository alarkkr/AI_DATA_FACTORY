import faiss
import numpy as np
import json
from ai_processing.embedding_engine import create_embedding

index = faiss.read_index("vector.index")

def search(query,k=5):

    vec = create_embedding(query)

    arr = np.array([vec]).astype("float32")

    D,I = index.search(arr,k)

    with open("knowledge_store.jsonl","r",encoding="utf-8") as f:

        records = [json.loads(line) for line in f]

    results = []

    for idx in I[0]:

        if idx < len(records):

            results.append(records[idx]["content"])

    return results
