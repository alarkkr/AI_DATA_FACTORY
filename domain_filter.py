ALLOWED_TOPICS=[
"machine learning",
"deep learning",
"artificial intelligence",
"reinforcement learning",
"neural network",
"robotics",
"computer vision",
"natural language processing",
"knowledge representation",
"planning",
"ai safety",
"evolutionary algorithms"
]

def allowed(topic):

    topic=topic.lower()

    for t in ALLOWED_TOPICS:
        if t in topic:
            return True

    return False
