#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ').strip().upper())

def lerA():
    return print('Quantidade de letra A: {}'.format(frase.count('A')))

def posiA():
    return print('Posição da primeira letra A da frase: {} '.format(frase.find('A') + 1))  

def posiAU():
    return print('Posição da ultima letra a da frase: {}'.format(frase.rfind('A') +1 ))
   
lerA()
posiA()
posiAU()