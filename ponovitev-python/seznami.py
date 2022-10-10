prazni_seznam = []

prazni_seznam2 = [int] * 10

seznam = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print (seznam[0])

print (seznam[-1])

print (seznam[1:3])

print (seznam[:3])

print (seznam[1:])

seznam1 = seznam[:]

print (seznam1)

for elem in seznam:
    print (elem)

seznam.append('y')

print (seznam)

print (seznam.index('y'))

print (seznam.count('y'))
