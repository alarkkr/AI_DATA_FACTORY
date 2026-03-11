import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor
from crawler.topic_queue import get_topics

HEADERS = {
    "User-Agent": "AI-Research-Bot/1.0 (Educational Project)"
}

MAX_PAGES = 20
THREADS = 5

def build_search_urls():

    topics = get_topics()

    urls = []

    for t in topics[:10]:

        query = t.replace(" ","_")

        urls.append(f"https://en.wikipedia.org/wiki/{query}")

    if not urls:

        urls.append("https://en.wikipedia.org/wiki/Artificial_intelligence")

    return urls


def fetch_page(url):

    try:

        r = requests.get(url, headers=HEADERS, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        return soup

    except Exception as e:

        print("Fetch error:", e)

        return None


def extract_links(soup):

    links = []

    for a in soup.find_all("a", href=True):

        link = a["href"]

        if link.startswith("/wiki/") and ":" not in link:

            links.append("https://en.wikipedia.org" + link)

    return links


def crawl_web():

    seeds = build_search_urls()

    visited=set()

    to_visit=seeds

    pages=[]

    with ThreadPoolExecutor(max_workers=THREADS) as executor:

        while to_visit and len(pages)<MAX_PAGES:

            batch=[]

            while to_visit and len(batch)<THREADS:

                url=to_visit.pop(0)

                if url not in visited:

                    visited.add(url)

                    batch.append(url)

            results=executor.map(fetch_page,batch)

            for soup in results:

                if soup is None:

                    continue

                pages.append(str(soup))

                links=extract_links(soup)

                for link in links:

                    if link not in visited and len(to_visit)<MAX_PAGES:

                        to_visit.append(link)

            time.sleep(1)

    return pages
