from core.system_analyzer import get_system_info

def calculate_agents():

    info = get_system_info()

    cpu = info["cpu_cores"]

    ram = info["ram_available_gb"]

    cpu_based = max(1, cpu // 3)

    ram_based = max(1, int(ram // 4))

    agents = min(cpu_based, ram_based)

    return agents
