import numpy as np

def scale(x):
    return (x - np.mean(x)) / np.std(x)
