from time import sleep
from random import randint

gameCount = cont = cont2 = n = 0
game = []
gameHint = []

print("-" * 40)
print(f"{'JOGO NA MEGA SENA':^33}")
print("-" * 40)
gameCount = int(input("Quantos jogos você quer que eu sorteie? "))
print("-=" * 4, end="")
print(f"   SORTEANDO {gameCount} JOGOS   ", end="")
print("-=" * 5)

while gameCount > cont2:
    while True:
        n = randint(1, 60)
        if n not in gameHint:
            gameHint.append(n)
            cont += 1
        if cont >= 6:
            break
    cont = 0
    cont2 += 1
    game.append(gameHint[:])
    gameHint.clear()
for c in range(0, gameCount):
    print(f"Jogo {c+1}: {sorted(game[c])}")
    sleep(1)

print("-" * 40)
print(f"{'< BOA SORTE >':^33}")
print("-" * 40)