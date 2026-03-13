from system_profiler import profile
from resource_model import AGENT_REQUIREMENTS,MAX_REASONING_AGENTS

RESERVED_CPU=2
RESERVED_RAM=4

def calculate():

    hw=profile()

    cpu_available=max(1,hw["cpu_cores"]-RESERVED_CPU)
    ram_available=max(1,hw["ram_gb"]-RESERVED_RAM)

    config={}

    for agent,req in AGENT_REQUIREMENTS.items():

        cpu_limit=int(cpu_available/req["cpu"])
        ram_limit=int(ram_available/req["ram"])

        config[agent]=max(1,min(cpu_limit,ram_limit))

    config["reasoning_agent"]=min(config["reasoning_agent"],MAX_REASONING_AGENTS)

    return config
