from random import randint
from time import sleep
from operator import itemgetter

game = dict()
listgame = list()
for c in range(1, 5):
    game[f"Jogador{c}"] = int(randint(1, 6))
print("Valores sorteados: ")
for k, v in game.items():
    print(f"   O {k} tirou {v} no dado.")
    sleep(0.5)
ranking = list()
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print("Ranking: ")
for i, v in enumerate(ranking):
    print(f"  O {v[0]} com {v[1]} ficou em {i+1}° lugar. ")