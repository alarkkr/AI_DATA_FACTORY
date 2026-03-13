from research_swarm import run_swarm
from paper_agent_swarm import run as paper_swarm
from training_dataset_builder import build
from topic_seed import seed

def think():

    print("\nAI Research Brain Running\n")

    seed()

    results=run_swarm()

    paper_swarm()

    build()

    for r in results:

        print("\nTopic:",r["topic"])
        print("\nHypothesis:\n",r["hypothesis"])
        print("\nQuestions:\n",r["questions"])

if __name__=="__main__":
    think()
