def manhattan(tocka1, tocka2):
    razdalja = 0.0
    for x_1, y_1 in zip(tocka1, tocka2):
        razdalja += abs(y_1 - x_1)
    return razdalja

# test
x1 = (1,2,3)
x2 = (3,4,5.5)

print ("Razdalja je: ", manhattan(x1, x2))
