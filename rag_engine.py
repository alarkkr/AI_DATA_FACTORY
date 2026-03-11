from database.vector_search import search
from rag_context import build_context
from rag_prompt import build_prompt
from ai_processing.llm_engine import ask_llm

def answer_question(question):

    docs = search(question,5)

    context = build_context(docs)

    prompt = build_prompt(question,context)

    answer = ask_llm(prompt)

    return answer
