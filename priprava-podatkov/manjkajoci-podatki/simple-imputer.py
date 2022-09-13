from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

df = pd.read_csv('../../podatkovne-zbirke/sport-manjkajoci.csv')

imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
imputer = imputer.fit(df[['average_hr']])
df['average_hr'] = imputer.transform(df[['average_hr']])
# za celotni podatkovni okvir
# df.iloc[:,:] = imputer.transform(df)
print (df)
