from crawler.web_crawler import crawl_web
from processing.html_cleaner import clean_html
from ai_processing.topic_decomposer import decompose
from ai_processing.knowledge_chunker import chunk_knowledge
from ai_processing.topic_extractor import extract_topics
from crawler.topic_queue import add_topics
from database.dataset_storage import store_units

def start_engine():

    pages = crawl_web()

    for page in pages:

        text = clean_html(page)

        topics = extract_topics(text)

        add_topics(topics)

        decomposed = decompose(text)

        chunks = chunk_knowledge(decomposed)

        store_units(chunks)

        print("Pipeline completed.")
