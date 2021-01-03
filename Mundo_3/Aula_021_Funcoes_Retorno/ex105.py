def notas(*notas, sit=False):
    """[função para receber e analisar notas de um aluno]
    Args:
        notas (lista): [pode ser passado quantas notas quiser]
        sit (bool, optional): [Mostrar ou não a situação do aluno]. Defaults to False.
    Returns:
        [dicionario]: [informações sobre as notas do aluno. Quantidade, maior, menor, media e situação]
    """
    maior = menor = media = 0
    for c, i in enumerate(notas):
        media += i
        if c == 0:
            maior = menor = i
        else:
            if i > maior: ## pode ser usado max(notas) para obter a maior nota
                maior = i
            if i < menor: ## pode ser usado min(notas) para obter a menor nota
                menor = i
    media = media / len(notas) ## pode ser usado sum(notas) para somar todos valores e sum(notas) / len(notas) para achar a media   
    qtdNotas = len(notas)
    if media >= 7:
        situacao = "Boa"
    elif media >= 5 < 7:
        situacao = "Razoável"
    else:
        situacao = "Ruim"
    ficha = {
        "total": qtdNotas,
        "maior": maior,
        "menor": menor,
        "media": media,
    }
    if sit:
        ficha["situacao"] = situacao
    return ficha


resp = notas(3.5, 10, 6.5, 1, 1, 4, sit=True)
help(notas)