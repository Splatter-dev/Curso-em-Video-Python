## Tratar infos

sexo = ""
idade = count_adult = count_men = count_mulher = 0
option = "S"

while True:
    if option == "N":
        break
    else:
        while option == "S":
            print("-"*20)
            print("CADASTRE UMA PESSOA")
            print("-"*20)
            idade = int(input("Idade: "))
            if idade > 18:
                count_adult += 1
            sexo = str(input("Sexo[M/F]: ")).strip().upper()
            while sexo != "M" and sexo != "F":
                sexo = str(input("Sexo[M/F]: ")).strip().upper()
            if sexo == "M":
                count_men += 1
            if idade < 20 and sexo == "F":
                count_mulher += 1    
            print("\n")
            option = input("Deseja continuar[S/N]? ").strip().upper()
            while option != "N" and option != "S":
                option = input("Deseja continuar[S/N]? ").strip().upper()

print(f'''{count_adult} Pessoas com mais de 18 anos.
{count_men} Homens cadastrados.
{count_mulher} Mulheres com menos de 20 anos.''')