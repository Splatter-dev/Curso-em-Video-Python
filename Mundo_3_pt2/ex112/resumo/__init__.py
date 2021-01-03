import ex112.operacoes
import ex112.formatacao


def tabela(valor=0, aumt=0, reduc=0):
    print("-"*35)
    print('RESUMO DO VALOR'.center(30))
    print("-"*35)
    print(f"{'Preço analisado:'} \t {ex112.formatacao.moeda(valor)}")
    print(f"{'Dobro do preço:'} \t {ex112.operacoes.dobro(valor,True)} ")
    print(
        f"Metade do preço: \t {ex112.operacoes.metade(valor, True)}")
    print(
        f"{aumt}% de aumento: \t {ex112.operacoes.acres(valor, aumt, True)}")
    print(
        f"{reduc}% de redução: \t {ex112.operacoes.decres(valor, reduc, True)}")
    print("-"*35)

