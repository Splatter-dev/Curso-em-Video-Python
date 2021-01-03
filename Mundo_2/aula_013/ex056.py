## Ler nome, idade e sexo de 4 pessoas. Calcular a média de todas as idades, mostrar o nome e a idade do homem mais velho e a quantidade de mulheres menores de 20 anos.

idadesoma = 0
nomehomemvel = ""
homemidade = 0
mulhermenor20 = 0

for i in range(1, 5):
    print("\n----{}º PESSOA----\n".format(i))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo(M, F): ")).strip().upper()

    idadesoma += idade
    media = idadesoma / 4

    if idade > homemidade and sexo == "M":
        homemidade = idade
        nomehomemvel = nome

    if idade < 20 and sexo == "F":
        mulhermenor20 += 1


print("\nA média de idade do grupo de pessoas é {:.1f}.".format(media))
print(
    "\nO homem mais velho do grupo se chama {} e a idade dele é {}.".format(
        nomehomemvel, homemidade
    )
)
print("\nTemos {} mulheres menores de 20 anos no grupo.\n".format(mulhermenor20))
