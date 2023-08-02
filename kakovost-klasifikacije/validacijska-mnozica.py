# povzeto po https://press.um.si/index.php/ump/catalog/book/643
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Naložimo podatke
podatki = load_iris(as_frame=True)

# Razdelimo podatke na začasne učne in testne
X_u1, X_t, y_u1, y_t = train_test_split(
    podatki.data, podatki.target, train_size=0.8, random_state=42)

# Začasno učne podatke razdelimo na dejansko učne in validacijske
X_u, X_v, y_u, y_v = train_test_split(
    X_u1, y_u1, train_size=0.75, random_state=42)

print("Velikost učne množice: ", X_u.shape)
print("Velikost učnih razredov: ", y_u.shape)
print("Velikost validacijske množice: ", X_v.shape)
print("Velikost validacijskih razredov: ", y_v.shape)
print("Velikost testne množice: ", X_t.shape)
print("Velikost testnih razredov: ", y_t.shape)
