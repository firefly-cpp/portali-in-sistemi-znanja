import os
import pandas as pd

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', '..', 'podatkovne-zbirke', 'plant-monitoring.json'
)
df = pd.read_json(path)

print(df.to_string())
