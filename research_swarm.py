from crawler.topic_queue import get_topics
from research_agent import run_research
from domain_filter import allowed

def run_swarm():

    topics=get_topics()

    results=[]

    for t in topics:

        if not allowed(t):
            continue

        r=run_research(t)

        if r is not None:
            results.append(r)

        if len(results)>=5:
            break

    return results
