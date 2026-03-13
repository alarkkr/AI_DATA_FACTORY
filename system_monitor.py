import psutil

def system_health():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    return cpu,ram
