import arxiv

SAVE_DIR="papers"

def download_papers(topic,max_results=10):

    search=arxiv.Search(
        query=topic,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    paths=[]

    for r in search.results():

        try:
            p=r.download_pdf(dirpath=SAVE_DIR)
            print("Downloaded:",p)
            paths.append(p)
        except:
            pass

    return paths
