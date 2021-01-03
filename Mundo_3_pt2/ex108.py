import ex108.operacoes
import ex108.formatacao

valor = float(input('Digite o preço: R$'))
print(
    f"A metade do valor {ex108.formatacao.moeda(valor)} é: {ex108.formatacao.moeda(ex108.operacoes.metade(valor))}")
print(
    f"O dobro do valor {ex108.formatacao.moeda(valor)} é: {ex108.formatacao.moeda(ex108.operacoes.dobro(valor))}")
print(
    f"O valor {ex108.formatacao.moeda(valor)} com 10% de acrescimo é: {ex108.formatacao.moeda(ex108.operacoes.acres(valor, 10))}")
print(
    f"O valor {ex108.formatacao.moeda(valor)} com 13% de decrescimo é: {ex108.formatacao.moeda(ex108.operacoes.decres(valor, 13))}")
