# primer iz knjige: https://press.um.si/index.php/ump/catalog/book/643
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import numpy as np

# Naložimo podatke
podatki = load_iris(as_frame = True)

# Izberemo eno instanco
izbrana = 133
X_izbrana = podatki.data.iloc[izbrana,:]
y_izbrana = podatki.target.iloc[izbrana]

# Izbrano instanco izločimo iz ostalih podatkov
X_ostali = podatki.data.drop(izbrana, axis = 0)
y_ostali = podatki.target.drop(izbrana)

# Standardiziramo podatke
standardizator = StandardScaler()
standardizator.fit(X_ostali)

X_ostali_s = standardizator.transform(X_ostali)
X_izbrana_s = standardizator.transform([X_izbrana])

for razdalja in ['euclidean', 'manhattan', 'cosine']:
    for k in [1, 3, 5]:
        knn = KNeighborsClassifier(n_neighbors=k, metric=razdalja)
        knn.fit(X_ostali_s, y_ostali)
        nap = knn.predict(X_izbrana_s)
        print (f'KNN metric = { razdalja }, k = { k } je napovedal razred { podatki.target_names[nap]} ')
