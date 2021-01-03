import ex107

valor = float(input('Digite o preço: R$'))
print(f"A metade do valor é: R${ex107.metade(valor):.2f}")
print(f"O dobro do valor é: R${ex107.dobro(valor):.2f}")
print(f"O valor com 10% de acrescimo é : R${ex107.acres(valor, 10):.2f}")
print(f"O valor com 13% de decrescimo é: R${ex107.decres(valor, 13):.2f}")
