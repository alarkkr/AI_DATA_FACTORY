from ai_processing.embedding_engine import create_embedding
from database.vector_db import store_vector
from knowledge_graph.graph_store import add_node
from utils.deduplicator import is_duplicate
import json

STORE_FILE = "knowledge_store.jsonl"

def store_units(units):

    with open(STORE_FILE,"a",encoding="utf-8") as f:

        for u in units:

            text = u["content"]

            if is_duplicate(text):
                continue

            vector = create_embedding(text)

            store_vector(vector)

            add_node(u["topic"],text)

            record={
                "topic":u["topic"],
                "content":text
            }

            f.write(json.dumps(record)+"\n")

            print("Stored:",u["topic"])
