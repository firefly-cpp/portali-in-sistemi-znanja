import os
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 
    '..', '..', 'podatkovne-zbirke', 'sport-manjkajoci.csv'
)
df = pd.read_csv(path)

imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
imputer = imputer.fit(df[['average_hr']])
df['average_hr'] = imputer.transform(df[['average_hr']])
# za celotni podatkovni okvir
# df.iloc[:,:] = imputer.transform(df)
print(df)
