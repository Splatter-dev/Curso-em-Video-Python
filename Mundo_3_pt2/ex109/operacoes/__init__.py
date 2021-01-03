import ex109.formatacao


def metade(valor, formt=False):
    metade = valor / 2
    return metade if not format else ex109.formatacao.moeda(metade)


def dobro(valor, formt=False):
    dobro = valor * 2
    return dobro if not format else ex109.formatacao.moeda(dobro)


def acres(valor, acrescimo=0, formt=False):
    acres = valor + (valor * acrescimo) / 100
    return acres if not format else ex109.formatacao.moeda(acres)


def decres(valor, decrescimo=0, formt=False):
    decres = valor - (valor * decrescimo) / 100
    return decres if not format else ex109.formatacao.moeda(decres)
