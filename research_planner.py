from knowledge_gap_detector import detect_gaps
from crawler.topic_queue import add_topics

def plan_research():

    gaps = detect_gaps()

    if not gaps:

        print("No knowledge gaps detected")

        return

    print("Knowledge gaps found:",gaps)

    add_topics(gaps)

    print("Topics added to crawler queue")
