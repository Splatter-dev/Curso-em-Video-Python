# Calcular valor da viagem. 0,50 centavos para viagens até 200km, acima de 200 0,45

dstviag = float(input('Qual a distancia da viagem? '))
print('A distancia da viagem é: {:.0f}Km'.format(dstviag))
preco = dstviag * 0.50 if dstviag <= 200 else dstviag * 0.45 # forma diferente de fazer. Operador ternario/ ifen line
print('Valor da viagem {}R$'.format(preco))

def dstdeci():
    if dstviag <= 200:
        calc200()
    else:
        calc200mais()

def calc200():
    valor = dstviag * 0.50
    print('O valor por Km é de R$0,50 para viagens de até 200Km. Sua viagem ficou no valor de: R${:.2f}0.\nObrigado!'.format(valor))

def calc200mais():
    valor = dstviag * 0.45
    print('O valor por Km é de R$0,45 para viagens acima de 200Km. Sua viagem ficou no valor de R${:.2f}.\nObrigado!'.format(valor))

# dstdeci()    
