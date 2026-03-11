from rag_engine import answer_question

print("Local AI Assistant Ready")

while True:

    q = input("\nAsk something: ")

    if q == "exit":
        break

    answer = answer_question(q)

    print("\nAI Answer:\n")

    print(answer)
