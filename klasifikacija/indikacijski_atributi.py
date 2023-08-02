# povzeto po https://press.um.si/index.php/ump/catalog/book/643
import pandas as pd

# Definiramo vsako instanco kot seznam atributov
cevljiA = [17, 231, 'da', 'rjavi']
cevljiB = [9, 119, 'ne', 'modri']
cevljiC = [12, 143, 'ne', 'črni']
cevljiD = [8, 112, 'ne', 'rjavi']
cevljiE = [11, 198, 'da', 'modri']
cevljiF = [15, 245, 'da', 'črni']

# Z združitvijo instanc ustvarimo DataFrame
podatki = pd.DataFrame([cevljiA, cevljiB, cevljiC, cevljiD, cevljiE, cevljiF],
                       columns=['Višina', 'Teža', 'Vodood', 'Barva'],
                       index=['cevlji A', 'cevlji B', 'cevlji C', 'cevlji D', 'cevlji E', 'cevlji F'])

print(podatki)

# Vse kategorične atribute spremenimo v indikacijske
podatki2 = pd.get_dummies(podatki)

print(podatki2)
