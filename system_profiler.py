import psutil
import platform

def profile():

    cpu_cores = psutil.cpu_count(logical=True)

    ram_gb = round(psutil.virtual_memory().total / (1024**3))

    disk_gb = round(psutil.disk_usage("/").total / (1024**3))

    info = {
        "cpu_cores": cpu_cores,
        "ram_gb": ram_gb,
        "disk_gb": disk_gb,
        "system": platform.system()
    }

    return info
