from reasoning_engine import reason

while True:

    q = input("Ask reasoning query: ").strip()

    if q == "":
        continue

    r = reason(q)

    print("\nReasoning result:\n")

    for k,v in r.items():
        print(k,":",v)

    print()
