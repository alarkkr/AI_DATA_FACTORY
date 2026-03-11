from core.system_analyzer import get_system_info
from core.capacity_planner import calculate_agents

info = get_system_info()

print("\nSYSTEM HARDWARE\n")

print("CPU cores:", info["cpu_cores"])
print("RAM total:", info["ram_total_gb"],"GB")
print("RAM available:", info["ram_available_gb"],"GB")

agents = calculate_agents()

print("\nRecommended crawler agents:", agents)
