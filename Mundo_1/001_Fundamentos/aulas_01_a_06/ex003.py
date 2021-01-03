numero_1 = int(input('Digite o primeiro numero: '))
numero_2 = int(input('Digite o segundo numero: '))
numero_res = numero_1 + numero_2

# print('A soma entre ', numero_1, 'e ', numero_2,' é igual a: ', numero_res) // sintaxe não indicada
print('A soma entre {} e {} é igual a: {}'.format(numero_1 ,numero_2 , numero_res))