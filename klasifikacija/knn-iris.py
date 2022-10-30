# primer iz knjige: https://press.um.si/index.php/ump/catalog/book/643
from sklearn.datasets import load_iris
import seaborn as sns
import matplotlib.pyplot as plt

# Naložimo podatke
podatki = load_iris(as_frame = True)

# Izberemo eno instanco
izbrana = 133

X_izbrana = podatki.data.iloc[izbrana,:]
y_izbrana = podatki.target.iloc[izbrana]

# Izbrano instanco izločimo iz ostalih podatkov
X_ostali = podatki.data.drop (izbrana , axis = 0)
y_ostali = podatki.target.drop (izbrana)

# najprej vizualiziramo

x_os , y_os = 0, 1

# Izrišemo ostale instance
sns.scatterplot (x = X_ostali.iloc[:,x_os],
                y = X_ostali.iloc[:,y_os],
                hue = podatki.target_names[y_ostali],
                palette = 'colorblind')

# Izrišemo eno izbrano instanco
sns.scatterplot(x = [X_izbrana.iloc[x_os]],
                y = [X_izbrana.iloc[y_os]],
                hue = ['Neznan'], style = ['Neznan'],
                markers = {'Neznan': '^'} )

plt.show()
