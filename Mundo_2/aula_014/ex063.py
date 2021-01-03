# Sequencia de fibonacci
# As primeiras squencias sempre serão 0 1 1
# Para obter a sequencia o numero atual soma com seu antecessor

seq = int(input("\nDigite quantas sequencias você quer: "))
num = 0
num2 = 1
num3 = 0
cont = 2 # Começa com 2 porque já fizemos as duas primeiras sequencias no print abaixo, antes do while.

print("{} → {} ".format(num, num2), end=" → ")

while cont <= seq:
    num3 = num + num2
    num = num2
    num2 = num3
    cont += 1
    if cont <= seq:
        print(" {}  → ".format(num3), end="")
    else:
        print("FIM")
print("\n")