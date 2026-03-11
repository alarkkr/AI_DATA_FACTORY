import psutil

MAX_CPU=80
MAX_RAM=80

def system_ok():

    cpu=psutil.cpu_percent()

    ram=psutil.virtual_memory().percent

    if cpu>MAX_CPU or ram>MAX_RAM:

        return False

    return True
