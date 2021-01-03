# Detector de menor e maior de idade. Mostrar quantidade de cada um

from datetime import date

menor = 0
maior = 0
anoatual = date.today().year
idade = 0

for i in range(0, 7):
    nasc = int(input("\nDigite o seu ano de nascimento: "))
    if anoatual - nasc < 21:
        idade = anoatual - nasc
        menor += 1
    else:
        maior += 1
print("\n{} pessoas maiores de idade e {} menores de idade.\n ".format(maior, menor))
