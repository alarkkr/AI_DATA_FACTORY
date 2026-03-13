import json
from ai_processing.embedding_engine import create_embedding
from database.vector_db import store_vector

STORE_FILE = "knowledge_store.jsonl"

def store_new_knowledge(topic, text):

    try:
        vector = create_embedding(text)

        store_vector(vector)

        record = {
            "topic": topic,
            "content": text
        }

        with open(STORE_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

        print("New knowledge stored:", topic)

    except Exception as e:
        print("Knowledge storage error:", e)
