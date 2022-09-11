import pandas as pd

trening = {
  "trajanje": [100, 150, 50],
  "dolzina": [55, 75, 23],
  "vzpon": [100, 300, None]
}

df = pd.DataFrame(trening)

print(df.isna())
