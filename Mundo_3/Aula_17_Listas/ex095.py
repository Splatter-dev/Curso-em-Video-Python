jogador = dict()
jogadores = list()
gols = []
totg = 0
idJogador = 1

while True:
    nome = str(input("Nome do jogador: "))
    partidasQtd = int(input(f"Quantas partidas {nome} jogou?  "))
    for i in range(1, partidasQtd + 1):
        g = int(input(f"Quantos gols na {i}° partida: "))
        totg += g
        gols.append(g)
    jogador = {
        "id": idJogador,
        "nome": nome,
        "partidas": partidasQtd,
        "gols": gols[:],
        "totaldegols": totg,
    }
    jogadores.append(jogador)
    gols.clear()
    totg = 0
    idJogador += 1
    while True:
        continuar = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
        if continuar in "SN":
            break
        print("ERRO! Selecione uma alternativa correta.")
    if continuar == "N":
        break
print("-=" * 30)

print(f"{'Cod.':>2} {'NOME':>2}     {'Gols':>2}     {'Total':>2}")
contagem = 1
for v in jogadores:
    print(f'{contagem}     {v["nome"]}      {v["gols"]}      {v["totaldegols"]}')
    contagem += 1
print("-=" * 30)

while True:
    pegarJogador = int(input("Mostrar dados de qual jogado(999 para sair)? "))
    if pegarJogador == 999:
        break
    if pegarJogador != len(jogadores):
        print(
            f"ERRO! Não existe jogador com o o código {pegarJogador}. Tente novamente."
        )
    print("-" * 40)
    for v in jogadores:
        if v["id"] == pegarJogador:
            print(f'--  LEVANTAMENTO DO JOGADOR {v["nome"]}  --')
            for c in range(0, v["partidas"]):
                print(f'No {c + 1}° jogo ele fez {v["gols"][c]} gols.')
            print("-" * 40)
print(" <-- VOLTE SEMPRE :) -->")
