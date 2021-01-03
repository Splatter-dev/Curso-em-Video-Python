# Somar apenas numeros pares digitados pelo usuario.
soma = 0
cont = 0
for mult in range(1, 7):
    num = int(input("\nDigite {}º numero: ".format(mult)))
    if num % 2 == 0:
        print("\nEsse numero é par! Vamos somar!")
        soma += num
        cont += 1
print("O valor da soma dos {} numeros pares é: {} ".format(cont, soma))
