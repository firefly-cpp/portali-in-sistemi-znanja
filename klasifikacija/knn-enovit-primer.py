# primer iz knjige: https://press.um.si/index.php/ump/catalog/book/643
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import numpy as np
from sklearn.preprocessing import StandardScaler

# Naložimo podatke
podatki = load_iris (as_frame = True)

# Izberemo več instanc
izbrane = [1, 31, 61, 91, 121]
X_izbrane = podatki.data.iloc[izbrane,:]
y_izbrane = podatki.target.iloc[izbrane]

# Izbrano instanco izločimo iz ostalih podatkov
X_ostali = podatki.data.drop (izbrane, axis = 0)
y_ostali = podatki.target.drop(izbrane)

# Standardiziramo podatke
standardizator = StandardScaler()
standardizator.fit(X_ostali)
X_ostali_s = standardizator.transform(X_ostali)
X_izbrane_s = standardizator.transform(X_izbrane)

# Zgradimo klasifikator in napovemo razrede
knn = KNeighborsClassifier(n_neighbors = 3, metric = 'euclidean')
knn.fit(X_ostali_s, y_ostali)
napovedi = knn.predict(X_izbrane_s)

for i, napoved, dejansko in zip(izbrane, napovedi, y_izbrane):
    print (f'Instanca { i } je klasificirana kot { podatki.target_names[napoved]} dejansko pa je {podatki.target_names[dejansko] }.')
