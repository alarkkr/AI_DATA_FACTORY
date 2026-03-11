import json

GRAPH_FILE = "knowledge_graph.json"

def add_node(topic,content):

    try:
        with open(GRAPH_FILE,"r") as f:
            graph = json.load(f)
    except:
        graph = {}

    if topic not in graph:
        graph[topic] = []

    graph[topic].append(content[:200])

    with open(GRAPH_FILE,"w") as f:
        json.dump(graph,f,indent=2)
