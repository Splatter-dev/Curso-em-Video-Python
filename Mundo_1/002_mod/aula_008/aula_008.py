# Explicação de como importar biblioteca

from math import sqrt, ceil, floor
import random
import emoji

# 1º Exemplo (importado da bb math > sqrt,ceil,)

n1rz = int(input('Digite um numero: '))
rz = sqrt(n1rz)

print('Olá. A raiz quadrada de {} é {:2f} '.format(n1rz, rz))



# 2º Exemplo (Usando biblioteca random)

n1rd = random.randint(1,10)

print('{}'.format(n1rd))


# 3º Usando biblioteca emoji (acessar python.org e ver documentacao de cada biblioteca para instalar)
print(emoji.emojize("Olá :grinning:", use_aliases=True))

