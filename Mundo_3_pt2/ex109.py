import ex109.formatacao
import ex109.operacoes


valor = float(input('Digite o preço: R$'))
print(
    f"A metade do valor {ex109.formatacao.moeda(valor)} é: {ex109.operacoes.metade(valor, True)}")
print(
    f"O dobro do valor {ex109.formatacao.moeda(valor)} é: {ex109.operacoes.dobro(valor, True)}")
print(
    f"O valor {ex109.formatacao.moeda(valor)} com 10% de acrescimo é: {ex109.operacoes.acres(valor, 10, True)}")
print(
    f"O valor {ex109.formatacao.moeda(valor)} com 13% de decrescimo é: {ex109.operacoes.decres(valor, 13, True)}")
