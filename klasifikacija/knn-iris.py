# primer iz knjige: https://press.um.si/index.php/ump/catalog/book/643
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Naložimo podatke
podatki = load_iris(as_frame = True)

# Izberemo eno instanco
izbrana = 133

X_izbrana = podatki.data.iloc[izbrana,:]
y_izbrana = podatki.target.iloc[izbrana]

# Izbrano instanco izločimo iz ostalih podatkov
X_ostali = podatki.data.drop (izbrana , axis = 0)
y_ostali = podatki.target.drop (izbrana)

# najprej vizualiziramo

x_os , y_os = 0, 1

# Inicializiramo klasifikator
knn = KNeighborsClassifier(n_neighbors = 5, metric = 'manhattan')

# Shranimo instance za primerjavo
knn.fit(X_ostali, y_ostali)

# Napovemo razred izbrane instance
napoved = knn.predict([ X_izbrana ])

print (f'KNN je napovedal , da je instanca razreda {podatki.target_names[napoved]}.')
print (f'Ta instanca je dejansko razreda {podatki.target_names [y_izbrana] }.')

# Izbrani instanci najdemo pet najbližjih sosedov
razdalje,sosedi = knn.kneighbors([X_izbrana], n_neighbors = 5 )
print (f'Pet najbližjih : {sosedi} ')
print (f'Razdalje od najbližjih do izbrane : { razdalje }')
