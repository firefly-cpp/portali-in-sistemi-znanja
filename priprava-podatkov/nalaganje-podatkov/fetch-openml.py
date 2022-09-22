from sklearn.datasets import fetch_openml

# nalozimo zbirko
# za vec podatkovnih zbirk obiscite https://www.openml.org/
zbirka = fetch_openml(name = "abalone")

# izpisemo znacilnice izbrane podatkovne zbirke
print (zbirka.feature_names)

# nalozimo zbirko v obliki DataFrame
zbirka2 = fetch_openml(name = "iris", as_frame = True)
print (zbirka2.target.head())
