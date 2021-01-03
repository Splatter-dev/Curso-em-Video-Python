import ex110.operacoes
import ex110.formatacao


def tabela(valor=0, aumt=0, reduc=0):
    print("-"*35)
    print('RESUMO DO VALOR'.center(30))
    print("-"*35)
    print(f"{'Preço analisado:'} \t {ex110.formatacao.moeda(valor)}")
    print(f"{'Dobro do preço:'} \t {ex110.operacoes.dobro(valor,True)} ")
    print(
        f"Metade do preço: \t {ex110.operacoes.metade(valor, True)}")
    print(
        f"{aumt}% de aumento: \t {ex110.operacoes.acres(valor, aumt, True)}")
    print(
        f"{reduc}% de redução: \t {ex110.operacoes.decres(valor, reduc, True)}")
    print("-"*35)
