# Entrada do Primeiro termo e a Razão de uma P.A. Achar a decimo termo do PA.

pt = int(input("\nDigite o 1º termo: "))
rz = int(input("Digite a razão: "))
decimotermo = pt + (10 - 1) * rz
print("\n")

for i in range(pt, decimotermo + 1, rz):
    print(" {} ".format(i), end="→")
print(" ACABOU!\n")
