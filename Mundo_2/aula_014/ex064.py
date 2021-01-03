## Somar e mostrar quantidade de numeros digitados ignorando o numero 999 que é o flag(numero para interromper o programa)  

num = cont = soma = 0

while num != 999:
    num = int(input("\nDigite um numero[999 para parar]: "))
    if num != 999:
        cont += 1
        soma += num
print("\nForam digitados {} números. O resultado da soma entre os números foi de: {}.".format(cont, soma))
