# povzeto po https://press.um.si/index.php/ump/catalog/book/643
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold

# Naložimo podatke
podatki = load_iris(as_frame=True)

# Stratificirana navzkrižna validacija s štirimi rezi

skf = StratifiedKFold(n_splits=4)

rez = 1  # S tem bomo šteli reze
instanca = 13  # Pregledovali bomo instanco na mestu 13

print(f'Zanima nas instanca { instanca } s podatki : ')
print(podatki.data.iloc[instanca, :])

for ucne, testne in skf.split(podatki.data, podatki.target):
    if instanca in ucne:
        print(f'Instanca { instanca } je v { rez } . delitvi v učni množici. ')
    elif instanca in testne:
        print(
            f'Instanca { instanca } je v { rez } . delitvi v testni množici. ')
    rez = rez + 1
