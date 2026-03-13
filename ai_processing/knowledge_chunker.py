import re

def chunk_knowledge(text):

    paragraphs = re.split(r"\n\s*\n", text)

    chunks=[]

    for p in paragraphs:

        p=p.strip()

        if len(p) < 200:
            continue

        chunk={
            "topic":"research",
            "content":p
        }

        chunks.append(chunk)

    return chunks
