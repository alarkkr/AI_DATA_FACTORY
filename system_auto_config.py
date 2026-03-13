from agent_capacity_calculator import calculate

def generate():

    config=calculate()

    print("\nAUTO SYSTEM CONFIGURATION\n")

    for k,v in config.items():

        print(k,":",v)

    return config
