from research_question_generator import generate_questions
from research_hypothesis_generator import generate_hypothesis
from topic_cleaner import clean_topic

def run_research(topic):

    topic=clean_topic(topic)

    if topic is None:
        return None

    print("Researching topic:",topic)

    questions=generate_questions(topic)
    hypothesis=generate_hypothesis(topic)

    return {
        "topic":topic,
        "questions":questions,
        "hypothesis":hypothesis
    }
