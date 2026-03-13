from autonomous_query_engine import solve

print("\nAI RESEARCH SYSTEM READY\n")

while True:

    q = input("Ask AI Researcher: ").strip()

    if q == "":
        continue

    result = solve(q)

    print("\nAI Answer\n")

    print(result["answer"])
