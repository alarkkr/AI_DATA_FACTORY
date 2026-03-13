from llm_reasoning_engine import reason_with_llm
from knowledge_coverage import coverage_score
from crawler_trigger import expand_crawling
from reasoning_memory import store_reasoning
from knowledge_writer import store_new_knowledge
from query_topic_extractor import extract_topics
from core.agent_manager import start_agents

THRESHOLD = 2000

def solve(query):

    score = coverage_score(query)

    if score < THRESHOLD:

        print("Knowledge insufficient -> expanding research")

        expand_crawling(query)

        start_agents()

    result = reason_with_llm(query)

    store_reasoning(query,result)

    topics = extract_topics(query)

    if "answer" in result:

        for t in topics:
            store_new_knowledge(t,result["answer"])

    return result
