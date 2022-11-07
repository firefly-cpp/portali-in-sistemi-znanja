# povzeto po https://press.um.si/index.php/ump/catalog/book/643
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Naložimo podatke
podatki = load_iris (as_frame = True)

# Razdelimo podatke na učne in testne
X_u, X_t, y_u, y_t = train_test_split ( podatki.data, podatki.target, train_size = 0.7, random_state = 42)
print ("Velikost učne množice: ", X_u.shape)
print ("Velikost učnih razredov: ", y_u.shape)
print ("Velikost testne množice: ", X_t.shape)
print ("Velikost testnih razredov: ", y_t.shape)
