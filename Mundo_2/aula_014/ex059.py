# Digitar dois numeros. Escolher uma opção no menu.

print("\n", "-=-" * 20)
print("Seja bem vindo ao programa de soma, multiplicação e numero maior.")
print("-=-" * 20)


num1 = 0
num2 = 0
result = 0
option = 0
num1 = int(input("\nDigite um numero: "))
num2 = int(input("\nDigite outro numero: "))

while option != 5:
    print("\nSelecione uma opção:")
    option = int(
        input(
            "\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n"
        )
    )
    if option == 1:
        result = num1 + num2
        print("\nO resultado da soma é: {}".format(result))
    if option == 2:
        result = num1 * num2
        print("\nA resultado da multiplicação é: {}".format(result))
    if option == 3:
        if num1 > num2:
            print("\n{} é maior que {}.".format(num1, num2))
        elif num1 == num2:
            print("\nOs numeros são iguais!")
        else:
            print("\n{} é maior que {}.".format(num2, num1))
    if option == 4:
        num1 = int(input("\nDigite um numero: "))
        num2 = int(input("\nDigite outro numero: "))
    if option > 5:
        print("\n Opção incorreta. Escolha novamente.")    