import faiss
import numpy as np
import os

dimension = 384
index_file = "vector.index"

if os.path.exists(index_file):
    index = faiss.read_index(index_file)
else:
    index = faiss.IndexFlatL2(dimension)

def store_vector(vec):

    arr = np.array([vec]).astype("float32")

    index.add(arr)

    faiss.write_index(index, index_file)

    print("Vector stored. Total:", index.ntotal)
