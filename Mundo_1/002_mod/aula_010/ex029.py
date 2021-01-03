# Programa que le a velocidade do automovel, sabendo que o limite de velocidade é 80
# Se passar do limite dispara uma elerta
# A cada 1 km acima do limite é cobrado uma multa de 7 reais

from time import sleep

print('O limite de velocidade é 80Km/h. Qual sua velocidade atual?')
veloat = int(input('Digite a sua velocidade atual: '))

def veloult():
    if veloat > 80:
        print('Processando...')
        sleep(3)
        print('Você ultrapassou a velocidade permitida! Você será multado!')
        velomul()
    print('Processando...')
    sleep(3)    
    print('Você está dentro do limite de velocidade. Tenha um bom dia :)')

def velomul():
    velocires = veloat -80
    multa = velocires * 7
    print('Você estáva a {}Km/h acima do permitido.'.format(velocires))
    print('Sua multa é de R${},00!'.format(multa))
    
veloult()        
