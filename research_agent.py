from hypothesis_generator import generate_hypothesis
from research_question_generator import generate_questions
from research_memory import store_insight

def run_research(topic):

    print("Researching topic:",topic)

    hypothesis = generate_hypothesis(topic)

    questions = generate_questions(topic)

    store_insight(topic,hypothesis)

    return {
        "topic":topic,
        "hypothesis":hypothesis,
        "questions":questions
    }
