from paper_ingest_pipeline import ingest
from crawler.topic_queue import get_topics
from system_auto_config import generate
import threading

def worker(topic):

    try:
        ingest(topic)
    except:
        pass

def run():

    config=generate()

    agents=config["paper_agent"]

    topics=get_topics()

    threads=[]

    for t in topics[:agents]:

        th=threading.Thread(target=worker,args=(t,))
        th.start()

        threads.append(th)

    for th in threads:
        th.join()
