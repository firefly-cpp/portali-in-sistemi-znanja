# povzeto po https://press.um.si/index.php/ump/catalog/book/643
from sklearn.metrics import recall_score

# Podamo dejanske razrede in napovedi klasifikatorja
y_dejanski = ['A', 'A', 'B', 'B', 'A', 'B']
y_napovedan = ['A', 'A', 'B', 'A', 'A', 'B']

# Izračunamo priklic obeh razredov
priklic_A = recall_score(y_dejanski, y_napovedan, pos_label='A')
priklic_B = recall_score(y_dejanski, y_napovedan, pos_label='B')

print(f'Priklic A: {priklic_A}')
print(f'Priklic B: {priklic_B}')
