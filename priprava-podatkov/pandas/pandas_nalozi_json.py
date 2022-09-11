import pandas as pd

df = pd.read_json('../../podatkovne-zbirke/plant-monitoring.json')

print(df.to_string())
