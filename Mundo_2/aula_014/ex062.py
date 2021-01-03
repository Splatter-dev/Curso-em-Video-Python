# Progressão Aritimetica. Programa pergunta se o usuario desja adicionar mais termos

pt = int(input("\nDigite o PRIMEIRO TERMO da PA: "))
rz = int(input("Digite a RAZÃO da PA: "))
contpa = 0
contuser = 10

while contpa < contuser:
    print("{} → ".format(pt), end="")
    contpa += 1 
    pt = pt + rz
    if contpa == contuser:
        print(" PRONTO!\n")
        # contpa = 0
        # contuser = 0
        contuser += int(input("PRONTO! Digite quantos termos mais você quer mostrar: "))
print("Programa encerrado! {} termos mostrados.\n".format(contpa))