import os
import pandas as pd

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', '..', 'podatkovne-zbirke', 'sportydatagen.csv'
)
df = pd.read_csv(path)

print(df)
