from random import randint
from time import sleep


def sorteia(sorteados):
    print("Sorteando 5 valores da lista: ", end="")
    for n in range(0, 5):
        num = randint(1, 10)
        sorteados.append(num)
        print(sorteados[n], end=" ", flush=True)
        sleep(0.2)
    print("PRONTO!")
    somaPar(sorteados)


def somaPar(sorteados):
    tot = 0
    print(f"Somando os valores pares da lista {sorteados}, temos: ", end="")
    for c in range(0, len(sorteados)):
        if sorteados[c] % 2 == 0:
            tot += sorteados[c]
    print(tot)


sorteados = []
sorteia(sorteados)
