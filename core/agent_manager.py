from system_auto_config import generate

def start_agents():

    config=generate()

    crawler_agents=config["crawler"]

    print("Launching",crawler_agents,"crawler agents")

    for i in range(crawler_agents):

        print("Crawler",i,"started")
