# povzeto po https://press.um.si/index.php/ump/catalog/book/643
from sklearn.metrics import precision_score

# Podamo dejanske razrede in napovedi klasifikatorja
y_dejanski = ['A', 'A', 'B', 'B', 'A', 'B']
y_napovedan = ['A', 'A', 'B', 'A', 'A', 'B']

# Izračunamo preciznost obeh razredov
preciznost_A = precision_score(y_dejanski, y_napovedan, pos_label='A')
preciznost_B = precision_score(y_dejanski, y_napovedan, pos_label='B')

print(f'Preciznost A: {preciznost_A}')
print(f'Preciznost B: {preciznost_B}')
