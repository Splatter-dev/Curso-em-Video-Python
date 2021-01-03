# Programa de calculo de IMC e categorização de acoedo com o IMC

print('\nOlá. Seja bem-vindo ao programa de calculo de IMC e categorização de acoedo com o IMC.')

peso = float(input('\nQual o seu peso?\n'))
altura = float(input('\nQual a sua altura?\n'))

imc = peso / (altura**2)

if imc < 18.5:
    print('\nVocê está abaixo do peso. Seu imc é: {:.2f}.\n'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('\nVocê está com o peso ideal. Seu imc é: {:.2f}.\n'.format(imc))
elif imc > 25 and imc <= 40:
    print('\nVocê está com sobrepeso. Seu imc é: {:.2f}.\n'.format(imc)) 
else:
    print('\nVocê está com obesidade morbida. Seu imc é: {:.2f}.\n'.format(imc))           