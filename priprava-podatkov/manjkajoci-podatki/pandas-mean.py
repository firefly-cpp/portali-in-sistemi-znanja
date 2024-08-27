import os
import pandas as pd

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', '..', 'podatkovne-zbirke', 'sport-manjkajoci.csv'
)
df = pd.read_csv(path)

df['average_hr'] = df['average_hr'].fillna(df['average_hr'].mean())

print(df)
