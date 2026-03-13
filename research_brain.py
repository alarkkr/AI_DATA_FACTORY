from research_swarm import run_swarm

def think():

    print("\nAI Research Brain Running\n")

    results = run_swarm()

    for r in results:

        print("\nTopic:",r["topic"])
        print("\nHypothesis:\n",r["hypothesis"])
        print("\nQuestions:\n",r["questions"])
