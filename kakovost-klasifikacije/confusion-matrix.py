# povzeto po https://press.um.si/index.php/ump/catalog/book/643
from sklearn.metrics import confusion_matrix

# Podamo dejanske razrede in napovedi klasifikatorja
y_dejanski = ['A', 'A', 'B', 'B', 'A', 'B']
y_napovedan = ['A', 'A', 'B', 'A', 'A', 'B']

# Izračunamo matriko zmede
tp, fn, fp, tn = confusion_matrix(
    y_dejanski, y_napovedan, labels=['A', 'B']).ravel()

print("tp: ", tp)
print("fn: ", fn)
print("fp: ", fp)
print("tn: ", tn)
