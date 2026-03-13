import psutil
import time

MAX_CPU = 95
MAX_RAM = 92

def system_ok():

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory().percent

    if cpu > MAX_CPU or ram > MAX_RAM:
        return False

    return True
