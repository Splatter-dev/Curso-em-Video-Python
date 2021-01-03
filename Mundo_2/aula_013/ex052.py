numero = int(input("\nDigite um numero: "))
print("\n")
conta = 0  # Variavel para contar quantas vezes o resto da divisão foi 0(resultado de quando o numero é divisivel)

for i in range(1, numero + 1):
    if numero % i == 0:
        print("\033[33m{}\033[m ".format(i), end="")
        conta += 1
    else:
        print("\033[31m{}\033[m ".format(i), end="")
print("\n")

if conta == 2:
    print(
        "O número foi divisivel por {} números. Ele é um número primo!\n".format(conta)
    )
else:
    print(
        "O número foi divisivel por {} números! Ele não é um número primo!\n".format(
            conta
        )
    )
