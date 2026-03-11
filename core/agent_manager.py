import multiprocessing
from core.engine import start_engine
from core.resource_guard import system_ok
from core.capacity_planner import calculate_agents

def run_agent(agent_id):

    if not system_ok():

        print("System overloaded, skipping agent")

        return

    print(f"Agent {agent_id} started")

    start_engine()

    print(f"Agent {agent_id} finished")

def start_agents():

    agents = calculate_agents()

    print(f"Launching {agents} crawler agents\n")

    processes = []

    for i in range(agents):

        p = multiprocessing.Process(target=run_agent,args=(i,))

        processes.append(p)

        p.start()

    for p in processes:

        p.join()

    print("All agents completed")
