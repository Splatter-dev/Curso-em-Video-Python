# Numeros impares multiplos/divisiveis por 3. A soma do todos os valores.

soma = 0
cont = 0

print('\nNumeros impares de 0 500, mutiplos de 3:\n')

for i in range(0,500, 3): # 3 usado para conseguir os multiplos de 3
    if i % 2 != 0: # Todo resto de divisão por 2 que da 0 é par. Se o resto for diferente de 0 é impar
        soma += i
        cont += 1
        print(i,end=' ')
print('\n\nSoma de todos os {} valores impares: {}'.format(cont, soma))
print('\n')