# Digitar um numero real(ex 5.5555) e mostrar sua porção iteira(5)

from math import trunc

n1 = float(input('Digite um numero real: '))

n1trun = trunc(n1)

print('O numero {}\nTruncado é {}'.format(n1,n1trun))