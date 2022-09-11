import pandas as pd

df = pd.DataFrame({

    'sport': ['kolesarstvo', 'kolesarstvo', 'tek', 'tek', 'tek', 'plavanje'],

    'dan': ['ponedeljek', 'ponedeljek', 'sreda', 'petek', 'petek', 'sobota'],

    'napor': [2, 2, 3, 3, 3, 3]
    })

print (df)

# odstranimo duplikate
#df = df.drop_duplicates()

#print (df)

# odstranimo duplikate glede na ime stolpca
#df = df.drop_duplicates(subset=['sport'])

#print (df)

#odstranimo glede na ime stolpca in ohranimo zadnjo ponovitev
#df = df.drop_duplicates(subset=['sport', 'dan'], keep='last')

#print (df)

#uporaba duplicated()

df = df.duplicated()

print (df)
