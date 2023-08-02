import pandas as pd

trening = {
    "trajanje": [100, 150, 50],
    "dolzina": [55, 75, 23],
    "vzpon": [100, 300, 250]
}

df = pd.DataFrame(trening)

print(df)

# df = df.drop(['trajanje'], axis=1)

# odstranimo glede na ime stolpca
# df = df.drop(columns="trajanje")

# odstranimo vrstice glede na indekse
# df = df.drop([0, 1])

print(df)
