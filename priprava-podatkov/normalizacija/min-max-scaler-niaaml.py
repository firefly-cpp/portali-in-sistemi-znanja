import os
from niaaml.data import CSVDataReader
from sklearn.preprocessing import MinMaxScaler

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

min_max = MinMaxScaler(feature_range=(0, 1))
novi_X = min_max.fit_transform(X)
print(novi_X)

# primer 2
X2 = [[10, 20], [30, 40], [150, 500], [350, 10], [800, 950]]

min_max2 = MinMaxScaler(feature_range=(0, 1))
novi_X2 = min_max2.fit_transform(X2)
print(novi_X2)
