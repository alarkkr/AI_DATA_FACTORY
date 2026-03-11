import schedule
import time
from core.agent_manager import start_agents

schedule.every(2).hours.do(start_agents)

while True:

    schedule.run_pending()

    time.sleep(60)
