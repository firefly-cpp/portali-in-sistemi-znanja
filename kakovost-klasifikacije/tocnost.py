# povzeto po https://press.um.si/index.php/ump/catalog/book/643
from sklearn.metrics import accuracy_score

# Podamo dejanske razrede in napovedi klasifikatorja
y_dejanski = ['A' ,'A' ,'B' ,'B' ,'A' ,'B']
y_napovedan = ['A' ,'A' ,'B' ,'A' ,'A' ,'B']

# Izračunamo točnost
tocnost = accuracy_score(y_dejanski, y_napovedan)

delez_napake = 1 - tocnost

# Izračunamo število pravilno klasificiranih (TP + TN)
st_pravilnih = accuracy_score(y_dejanski, y_napovedan, normalize = False)
print (f'Točnost : { tocnost } ')
print (f'Delež napake: { delez_napake } ')
print (f'Število pravilnih: { st_pravilnih }')
