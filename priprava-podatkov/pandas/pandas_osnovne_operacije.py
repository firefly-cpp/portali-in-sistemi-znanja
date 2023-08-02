import pandas as pd

trening = {
    "trajanje": [100, 150, 50],
    "dolzina": [55, 75, 23],
    "vzpon": [100, 300, 250]
}

df = pd.DataFrame(trening)

# izberemo stolpec 'vzpon'
# df = df[['vzpon']]
# print(df)

# izberemo vrstico
# vrstica = df.loc[1]
# print(vrstica)
