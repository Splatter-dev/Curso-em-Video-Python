# Pedir um numero e um formato de conversão. Binario, octal e hexadecimal

def bina():
    parastr = str(bin(numero))
    # print(bin(numero))
    print('\nO valor da conversão para binário é: {}\n'.format(parastr[2:]))

def octa():
    # print(oct(numero))
    parastr = str(oct(numero))
    print('\nO valor da conversão para Octal é de: {}\n'.format(parastr[2:]))

def hexac(): 
    parastr = str(hex(numero))
    # print(hex(numero)) 
    print('\nO valor da conversão para Hexadecimal é: {}\n'.format(parastr[2:].upper()))   


print('\nOlá. Seja bem-vindo ao programa de conversão de numeros.')
numero  = int(input('Digite um numero: '))
tipo = str(input('\nEscolha a opção para conversão:\n\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n\nOpção: ')).strip().upper()

if tipo[0] == '1':
    bina()
elif tipo[0] == '2':
    octa()
elif tipo[0] == '3':
    hexac()
else:
    print('Opção não exixtente. Escoha novamente...')    
