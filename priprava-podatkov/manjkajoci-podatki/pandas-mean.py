import pandas as pd

df = pd.read_csv('../../podatkovne-zbirke/sport-manjkajoci.csv')

df['average_hr'] = df['average_hr'].fillna(df['average_hr'].mean())

print(df)
