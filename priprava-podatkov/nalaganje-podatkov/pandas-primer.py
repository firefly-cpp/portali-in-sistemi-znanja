import pandas as pd

zbirka = pd.read_csv("../../podatkovne-zbirke/dataset.csv")

print(zbirka.head())

print("Stevilo vrstic v podatkovni zbirki: ", (len(zbirka)))
