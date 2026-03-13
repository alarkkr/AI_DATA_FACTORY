import time
from training_dataset_builder import build

print("Dataset generator running")

while True:

    build()

    time.sleep(3600)
