def metade(valor):
    metade = valor / 2
    return metade


def dobro(valor):
    dobro = valor * 2
    return dobro


def acres(valor, acrescimo=0):
    acres = valor + (valor * acrescimo / 100) 
    return acres


def decres(valor, decrescimo=0):
    decres = valor - (valor * decrescimo / 100) 
    return decres
