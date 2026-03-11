from fastapi import FastAPI

app=FastAPI()

@app.get("/status")
def status():

    return {
        "crawler":"active",
        "vector_db":"ready",
        "knowledge_graph":"active"
    }
