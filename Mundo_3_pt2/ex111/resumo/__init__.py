import ex111.operacoes
import ex111.formatacao


def tabela(valor=0, aumt=0, reduc=0):
    print("-"*35)
    print('RESUMO DO VALOR'.center(30))
    print("-"*35)
    print(f"{'Preço analisado:'} \t {ex111.formatacao.moeda(valor)}")
    print(f"{'Dobro do preço:'} \t {ex111.operacoes.dobro(valor,True)} ")
    print(
        f"Metade do preço: \t {ex111.operacoes.metade(valor, True)}")
    print(
        f"{aumt}% de aumento: \t {ex111.operacoes.acres(valor, aumt, True)}")
    print(
        f"{reduc}% de redução: \t {ex111.operacoes.decres(valor, reduc, True)}")
    print("-"*35)

