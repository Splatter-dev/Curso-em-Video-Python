# Jogo de adivinhar o numero entre 0 e 5
from time import sleep
from random import randint

numAdivinha = randint(0, 5)

def tentAdv(): 
    print('-=-' *15)
    print('Tente adivinhar um numero de 0 a 5! ')
    print('-=-' *15)
    numero = int(input('Digite um numero: '))
    print('Processando...')
    sleep(1)
    if numero == numAdivinha:
        print(':) '*10)
        print('Voce acertou!!\nO numero que você escolheu é {} e o numero sorteado é {}!'.format(numero, numAdivinha))
    else:
        print(':( '*10)
        print('Errado! O numero sorteado foi: {}'.format(numAdivinha))

tentAdv()        