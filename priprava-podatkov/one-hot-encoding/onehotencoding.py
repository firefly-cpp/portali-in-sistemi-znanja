from sklearn.preprocessing import OneHotEncoder
from numpy import asarray

sport = asarray([['plavanje'], ['kolesarjenje'], ['tek']])
encoder = OneHotEncoder(sparse=False)
e_sport = encoder.fit_transform(sport)
print(sport)
print(e_sport)
