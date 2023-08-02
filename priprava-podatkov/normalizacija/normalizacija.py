import os
from niaaml.data import CSVDataReader
from sklearn import preprocessing

# NiaAML nam nudi razred CSVDataReader za enostavno nalaganje podatkovnih zbirk
data_reader = CSVDataReader(
    src=os.path.dirname(os.path.abspath(__file__)) + "/dataset.csv",
    has_header=False,
    contains_classes=True,
)

X = data_reader.get_x()
Y = data_reader.get_y()

# izpis x in y polj
print(X)
print(Y)

normaliziran_X = preprocessing.normalize(X)

# izpis normalizacije
print(normaliziran_X)
