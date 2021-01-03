#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um numero de 0 9999: '))
u  = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
milh = numero // 1000
 

print('Unidade: {}'.format(u)) # Mostra o ultimo
print('Dezena: {}'.format(dez)) # 
print('Centena: {}'.format(cen)) 
print('Milhar: {}'.format(milh))




# Outra opção. Essa irá adicionar sempre 5 casas, tendo assim sobra para as 4 casas que queremos encontrar

# n = int(input('Digite um número entre 0 e 9999: '))
# n2 = str(int(10000 + n))
# print(n2)
# print('O número {} possui, {} milhares.'.format(n, n2[1]))
# print('O número {} possui, {} centenas. '.format(n, n2[2]))
# print('O número {} possui, {} dezenas. '.format(n, n2[3]))
# print('O número {} possui, {} unidades.'.format(n, n2[4]))