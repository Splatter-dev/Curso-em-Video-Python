# Ler ano de nascimento e falar quanto tempo falta, passou e se já estamos no ano de alistameto.

from datetime import date



print('\nOlá. Seja bem vindo ao programa de alistamento.')
anonasc = int(input('\nDigite o seu ano de nascimento: '))
print('\nQual o seu sexo?\n1 - Masculino\n2 - Feminino\n')
sexo = int(input('Digite a opção: '))
anoatual = date.today().year
idade = anoatual - anonasc

def masc():
    if idade == 18:
        print('\nVocê deve se alistar esse ano.\n')
    elif idade < 18:
        tempfal = 18 - idade
        anoalis = anonasc + 18
        print('\nFaltam {} anos para o seu alistamento. Seu alistamento será em {}.\n'.format(tempfal, anoalis))    
    else:
        tempexc = idade - 18
        anoalis = date.today().year - tempexc 
        print('Você está atrasado {} anos para o alistamento!'.format(tempexc))
        print('Seu alistamento foi em {}.\n'.format(anoalis))


if sexo == 1:
    print('\nQuem nasceu em {} tem {} anos em 2020.'.format(anonasc, idade))
    masc()
else:
    print('\nVocê não precisa se alistar!\n')    

