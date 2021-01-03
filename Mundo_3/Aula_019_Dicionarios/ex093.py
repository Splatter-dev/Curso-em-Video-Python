campeonato = dict()
gols = []
totg = 0
nome = str(input("Nome: "))
campeonato["nome"] = nome
partidasQtd = int(input(f"Quantas partidas {nome} jogou?  "))

for i in range(1, partidasQtd + 1):
    g = int(input(f"Quantos gols na {i}° partida: "))
    totg += g
    gols.append(g)
campeonato["gols"] = gols
campeonato["total"] = totg
print("-=" * 27)
print(campeonato)
print("-=" * 27)
for k, v in campeonato.items():
    print(f"O campo {k} tem o valor {v}.")
print("-=" * 20)

print(f"O jogador {nome} jogou {partidasQtd} partidas.")
for i in range(0, partidasQtd):
    print(f"    => Na partida {i + 1}, fez {gols[i]} gols.")
print(f"Foi um total de {totg}.")    