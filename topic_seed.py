from crawler.topic_queue import add_topics
from ai_topic_generator import generate

def seed():

    topics=generate()

    print("Seeding topics:",topics)

    add_topics(topics)
