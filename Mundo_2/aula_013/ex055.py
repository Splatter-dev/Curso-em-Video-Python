# Ler o pesso de 5 pessoas e falar qual foi o maior e menor peso.

maiorp = 0
menorp = 0

for pesq in range(1, 6):
    peso = float(input("\nDigite o peso da {}ª: ".format(pesq)))
    if pesq == 1:  # Passar o primeiro valor para a variavel menorp para poder fazer a comparação
        menorp += peso
        maiorp += peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso

print(
    "\nO maior peso foi de {:.1f}kg e o menor foi de {:.1f}kg\n".format(maiorp, menorp)
)
