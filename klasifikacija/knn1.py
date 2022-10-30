# primer iz knjige: https://press.um.si/index.php/ump/catalog/book/643
from sklearn.neighbors import KNeighborsClassifier

klasif = KNeighborsClassifier(n_neighbors = 3, metric = 'manhattan')

# klasif.fit (X_u,y_u)
# napovedi = klasif.predict (X_t)

# klasif.fit(X_u, y_u)
# razdalje, sosedi = klasif.kneighbors (nove_instance, n_neighbors = 3)
