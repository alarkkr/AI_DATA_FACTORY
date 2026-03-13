from ai_processing.knowledge_chunker import chunk_knowledge
from database.dataset_storage import store_units

def process_paper(text):

    chunks = chunk_knowledge(text)

    store_units(chunks)

    print("Paper knowledge stored")
