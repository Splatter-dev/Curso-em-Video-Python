numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

numero_ad = numero1 + numero1
numero_sb = numero1 - numero1
numero_mt = numero1 * numero1
numero_dv = numero1 / numero1
numero_pt = numero1 ** numero2
numero_dvi = numero1 // numero2
numero_dvr = numero1 % numero2

print('A soma entre {} e {} é igual a: {}'.format(numero1 ,numero2 , numero_ad), end=' >>>>> ')
print('A subtraçã0 entre o numero {} e o numero {} é igual a {}'.format(numero1, numero2, numero_sb))
# print('A multiplicação entre o numero {} e o numero {} é igual a {}'.format(numero1, numero2, numero_mt))
# print('A divisão entre o numero {} e o numero {} é igual a {:.3f}'.format(numero1, numero2, numero_dv))
# print('A valor da potencia é {}'.format(numero_pt))
# print('O valor da divisão inteira é {}'.format(numero_dvi))
# print('O valor do resto da divisão é {}'.format(numero_dvr))