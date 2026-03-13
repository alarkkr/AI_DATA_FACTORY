import time
from autonomous_research_loop import run_cycle

print("Autonomous research daemon started")

while True:

    run_cycle()

    time.sleep(1800)
