import os
import pandas as pd

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', '..', 'podatkovne-zbirke', 'dataset.csv'
)
zbirka = pd.read_csv(path)

print(zbirka.head())

print("Stevilo vrstic v podatkovni zbirki: ", (len(zbirka)))
