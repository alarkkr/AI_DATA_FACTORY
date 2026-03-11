from bs4 import BeautifulSoup

def clean_html(html):

    soup = BeautifulSoup(html,"html.parser")

    paragraphs = soup.find_all("p")

    text_blocks = []

    for p in paragraphs:
        text = p.get_text().strip()

        if len(text) > 50:
            text_blocks.append(text)

    return " ".join(text_blocks)
