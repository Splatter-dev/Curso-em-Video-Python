# Ler o comprimento de 3 medidas e dizer se pode ou nãp formar um triangulo.


def ladostri():
    if a == b == c:
        print('Esse é um triangulo Equilátero') 
    # elif (a == b and a !=  c and c != b) or (a == c and a != b and c != b) or (b == c and b != a and c != a) or (c == a and c != b and b != a):
    #     print('\nEsse é um triangulo Isósceles.')
    elif a != b != c != a:    
        print('\nEsse é um triangulo Escaleno.') # Comparando primeiro todos os lados iguais e diferentes, oq eu sobra é o com dois lados iguais que é o mais complciado de fazer. Assim simplifica o cidigo e alogica.
    else:
        print('Esse é um triangulo Isósceles.')        



print('-=-'*10)
print('ANALISADOR DE TRIANGULO.')
print('-=-'*10)

a = float(input('Digite a medida do segmento A: '))
b = float(input('Digite a medida do segmento B: '))
c = float(input('Digite a medida do segmento C: '))


if b - c  < a < b + c and a -c < b < a + c and a - b < c < a + b:
    print('\nDa pra formar um triangulo!')
    ladostri()
else:
    print('\nNão da para formar um triangulo!')