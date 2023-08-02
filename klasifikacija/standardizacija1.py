# primer iz knjige: https://press.um.si/index.php/ump/catalog/book/643
from sklearn.datasets import load_iris

# Naložimo podatke
podatki = load_iris(as_frame=True)

print('Povprečja pred standardizacijo: ')
print(podatki.data.mean(axis=0))
print('Standardni odkloni pred standardizacijo: ')
print(podatki.data.std(axis=0))
