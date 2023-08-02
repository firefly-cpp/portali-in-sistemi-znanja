import numpy as np


def evklid(tocka1, tocka2):
    return np.sqrt(np.sum(np.square(tocka1 - tocka2)))


# test
tocka1 = np.array((1, 2, 3))
tocka2 = np.array((3, 4, 5.5))
print("Evklidova razdalja: ", evklid(tocka1, tocka2))
