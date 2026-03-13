import time
from research_brain import think

print("Autonomous research daemon started")

while True:

    think()

    time.sleep(1800)
