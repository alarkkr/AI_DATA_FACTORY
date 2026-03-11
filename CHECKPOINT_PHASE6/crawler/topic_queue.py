TOPIC_FILE = "topics.txt"

def add_topics(topics):

    with open(TOPIC_FILE,"a") as f:
        for t in topics:
            f.write(t+"\n")

def get_topics():

    try:
        with open(TOPIC_FILE,"r") as f:
            return list(set(f.read().splitlines()))
    except:
        return []
