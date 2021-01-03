# Mostrar se o numero é impar o par


numero = int(input('Digite um numero: '))

def imparpar():
    if numero % 2 == 0: # resto da divisão de um numero par é 00
        print('O numero {} é par!'.format(numero))
    else:
        print('O numero {} é impar!'.format(numero))        

imparpar()        