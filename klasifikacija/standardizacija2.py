# primer iz knjige: https://press.um.si/index.php/ump/catalog/book/643
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Naložimo podatke
podatki = load_iris(as_frame=True)

# Inicializacija standardizatorja
std = StandardScaler()

# Izračunamo povprečja in standardne odklone atributov
std.fit(podatki.data)

# Standardizacija podatkov
stand_podatki = std.transform(podatki.data)

# stand_podatki = std.fit_transform(podatki.data)

print('Povprečja po standardizaciji: ')
print(stand_podatki.mean(axis=0))
print('Standardni odkloni po standardizaciji: ')
print(stand_podatki.std(axis=0))
