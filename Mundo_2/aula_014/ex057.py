# Programa forçar o usuario a digitar M ou F

sexo = ""

while sexo != "M" and "F":
    sexo = str(input("\nDigite o sexo da pessoa: ")).upper().strip()
    if sexo[0] != "M" and sexo[0] != "F":
        print("\nDigite o valor correto!")
    else:
        if sexo[0] == "M":
            print("\nSexo masculino resitrado com sucesso!")
        if sexo[0] == "F":
            print("\nSexo feminino registrado com sucesso!")
