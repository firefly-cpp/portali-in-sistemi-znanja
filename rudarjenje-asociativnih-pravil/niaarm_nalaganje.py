import os
import pandas as pd
from niaarm import Dataset

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', 'podatkovne-zbirke', 'Abalone.csv'
)
df = pd.read_csv(path)

data = Dataset(df)
print(data)
