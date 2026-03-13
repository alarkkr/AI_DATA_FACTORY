from research_planner import plan_research
from core.agent_manager import start_agents

def run_cycle():

    print("\n--- RESEARCH CYCLE START ---\n")

    start_agents()

    plan_research()

    print("\n--- RESEARCH CYCLE COMPLETE ---\n")

if __name__ == "__main__":

    run_cycle()
