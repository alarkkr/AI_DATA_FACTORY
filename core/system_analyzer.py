import psutil

def get_system_info():

    cpu_cores = psutil.cpu_count(logical=True)

    ram_total = psutil.virtual_memory().total / (1024**3)

    ram_available = psutil.virtual_memory().available / (1024**3)

    return {
        "cpu_cores": cpu_cores,
        "ram_total_gb": round(ram_total,2),
        "ram_available_gb": round(ram_available,2)
    }
