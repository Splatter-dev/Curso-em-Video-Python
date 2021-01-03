def ficha(nome="", gols=0):
    """[summary]
    Args:
        nome (str, optional): [nome do jogador]. Defaults to "".
        gols (int, optional): [quantidade de gols do jogador]. Defaults to 0.
    Returns:
        [type]: [description]
    """
    if nome == "":
        nome = "<jogador desconhecido>"
    if gols == "" or not gols.isnumeric():
        gols = "0"
    impri = print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")
    return impri


print("-=" * 30)
nomeJogador = str(input("Digite o nome do jogador: ")).strip()
golsDoJogador = str(input("Quantidade de gols do jogador: ")).strip()
impri = ficha(nomeJogador, golsDoJogador)
