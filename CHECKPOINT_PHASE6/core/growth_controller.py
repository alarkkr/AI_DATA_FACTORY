MAX_AUTO = 10**12
MAX_LIMIT = 10**27

def check_growth(size):

    next_size=size*10

    if next_size>MAX_LIMIT:
        return "STOP"

    if next_size>MAX_AUTO:
        return "PERMISSION_REQUIRED"

    return "AUTO_EXPAND"
