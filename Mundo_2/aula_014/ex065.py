# Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = option = cont = soma = menor = maior = 0

while option != 2:
    cont += 1
    num = int(input("\nDigite um numero: "))
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    soma += num
    option = int(
        input("\nVocê quer continuar?\n[1] - SIM\n[2] - NÃO\nDigite a resposta: ")
    )
    if option != 1 and option != 2:
        cont = soma = menor = maior = 0
        print("Alternativa incorreta. Programa reiniciado.")
media = soma / cont

print(
    "\nMédia: {:.2f}\nSoma: {}\nMenor: {}\nMaior: {}\nQuandidade: {}".format(
        media, soma, menor, maior, cont
    )
)
