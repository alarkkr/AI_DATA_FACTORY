from training_manager import ready

def check():

    if ready():

        print("Dataset large enough for model training")

    else:

        print("Dataset not large enough yet")
