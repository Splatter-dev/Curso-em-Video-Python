# Comparar 2 numeros e falar qual é o maior ou se são iguais


print('\nOlá. Seja bem-vindo(a) ao programa de comparação de numeros.')
numero1 = int(input('\nDigite o valor do primeiro numero: '))
numero2 = int(input('Digite o valor do segundo numero: '))

if numero1 > numero2:
    numeromaior = numero1
    print('\nO primeiro numero é o maior!\n')
elif numero2 > numero1:
    numeromaior = numero2
    print('\nO segundo numero é o maior!\n')
else:
    print('\nOs numeros são iguais!\n')