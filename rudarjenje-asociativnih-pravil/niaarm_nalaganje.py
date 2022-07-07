import pandas as pd
from niaarm import Dataset

df = pd.read_csv('../podatkovne-zbirke/Abalone.csv')

data = Dataset(df)
print(data)
