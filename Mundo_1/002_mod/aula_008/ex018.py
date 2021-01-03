# Calcular Seno, Cosseno e Tangente de um Angulo

import math

n1 = int(input('Digite o valor do angulo: '))
n1sen = math.sin(math.radians(n1))
n1cos = math.cos(math.radians(n1))
n1tan = math.tan(math.radians(n1))

print('{}°: \nSeno {:.2f}\nCoseno {:.2f}\nTangente {:.2f}'.format(n1,n1sen,n1cos,n1tan))