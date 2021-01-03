# Digitar o primeiro termo da PA e a RAZÃO.

pt = int(input("\nDigite o PRIMEIRO TERMO da PA: "))
rz = int(input("Digite a RAZÃO da PA: "))
contpa = 0

print("\n{} ".format(pt), end="")
while contpa < 9:
    contpa += 1
    pt = pt + rz
    print(" → {} ".format(pt), end="")
print(" → FIM!")    
print("\n")   