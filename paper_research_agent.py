from crawler.topic_queue import get_topics
from paper_ingest_pipeline import ingest

def run():

    topics=get_topics()

    if not topics:
        return

    for t in topics[:10]:

        print("Researching papers:",t)

        ingest(t)
