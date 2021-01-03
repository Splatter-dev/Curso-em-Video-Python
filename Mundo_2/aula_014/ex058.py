# Jogo de adivinhar. O usuario tenta adivinhar o numero que a mquina de escolhe(de 1 a 10)
# O programa só para quando o usario acertae mostra quantas tentatias o usuario fez

from random import randint
from time import sleep

nummachine = randint(0, 10)
numuser = 0
numcount = 0

print("\n","-=-" * 20)
print("Tente adivinhar o numero que a maquina escolheu. De 0 à 10! ")
print("-=-" * 20)

while numuser != nummachine:
    numuser = int(input("\nDigite um numero de 0 à 10: "))
    if numuser > nummachine:
        numcount += 1
        print("\nMenos... Tente novamente!")
    elif numuser < nummachine:
        numcount += 1
        print("\nMais...Tente novamente!")        
    else:
        print(
            "\nVocê acertou! O numero escolhido por você foi o {} e o da maquina foi {}.".format(
                numuser, nummachine
            )
        )
        print("\nVocê precisou de {} tentativas para acertar.".format(numcount))
        