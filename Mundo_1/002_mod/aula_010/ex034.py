# Aumento de salário de acordo com o valor do salário

salario = float(input('Digite o valor do seu salário: '))


def aumento10():
    if salario > 1250:
        aumento = (salario * 10) / 100    
        nvsalario = salario + aumento
        print('Seu aumento foi de 10%, R${:.2f} e seu novo salário é de R${:.2f}'.format(aumento, nvsalario))
    else:
        aumento15()    

def aumento15():
    aumento = (salario * 15) / 100    
    nvsalario = salario + aumento
    print('Seu aumento foi de 15%, R${:.2f} e seu novo salário é de R${:.2f}'.format(aumento, nvsalario))    

aumento10()    