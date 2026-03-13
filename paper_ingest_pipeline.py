from paper_downloader import download_papers
from pdf_reader import extract_text
from paper_processor import process_paper

def ingest(topic):

    pdfs = download_papers(topic)

    for p in pdfs:

        text = extract_text(p)

        process_paper(text)
