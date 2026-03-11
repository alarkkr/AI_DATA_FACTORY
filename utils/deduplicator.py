import hashlib
from utils.text_normalizer import normalize

HASH_FILE="hash_index.txt"

def compute_hash(text):

    text=normalize(text)

    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_hashes():

    try:
        with open(HASH_FILE,"r") as f:
            return set(f.read().splitlines())
    except:
        return set()


def save_hash(h):

    with open(HASH_FILE,"a") as f:
        f.write(h+"\n")


def is_duplicate(text):

    h=compute_hash(text)

    hashes=load_hashes()

    if h in hashes:
        return True

    save_hash(h)

    return False
