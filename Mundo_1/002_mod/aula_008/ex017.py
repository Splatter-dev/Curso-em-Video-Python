# Ler o cateto oposto e o cateto adjacente e calcular a hipotenusa

from math import hypot

catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
hyp = hypot(catop, catad)


print(hyp)
