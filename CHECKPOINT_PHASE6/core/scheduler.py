import schedule
import time
from core.engine import start_engine

schedule.every(2).hours.do(start_engine)

while True:

    schedule.run_pending()

    time.sleep(60)
