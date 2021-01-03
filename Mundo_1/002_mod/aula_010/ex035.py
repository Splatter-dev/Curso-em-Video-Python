# Ler o comprimento de 3 medidas e dizer se pode ou nãp formar um triangulo.

print('-=-'*10)
print('ANALISADOR DE TRIANGULO.')
print('-=-'*10)

a = float(input('Digite a medida do segmento A: '))
b = float(input('Digite a medida do segmento B: '))
c = float(input('Digite a medida do segmento C: '))

def triang():
    if b - c  < a < b + c and a -c < b < a + c and a - b < c < a + b:
        print('Da pra formar um triangulo!')
    else:
        print('Não da para formar um triangulo!')


triang()        
