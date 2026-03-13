from crawler.topic_queue import get_topics
from research_agent import run_research

def run_swarm():

    topics = get_topics()

    results = []

    for t in topics[:5]:

        r = run_research(t)

        results.append(r)

    return results
