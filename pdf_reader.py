import fitz
import os

OUT_DIR="paper_text"

def extract_text(pdf_path):

    doc=fitz.open(pdf_path)

    text=""

    for page in doc:
        text+=page.get_text()

    name=os.path.basename(pdf_path)+".txt"

    out=os.path.join(OUT_DIR,name)

    with open(out,"w",encoding="utf-8") as f:
        f.write(text)

    print("Text extracted:",out)

    return text
