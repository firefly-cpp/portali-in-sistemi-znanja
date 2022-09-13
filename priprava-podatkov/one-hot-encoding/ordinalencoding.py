from sklearn.preprocessing import OrdinalEncoder
from numpy import asarray

sport = asarray([['plavanje'], ['kolesarjenje'], ['tek']])
encoder = OrdinalEncoder()
e_sport = encoder.fit_transform(sport)
print(sport)
print(e_sport)
