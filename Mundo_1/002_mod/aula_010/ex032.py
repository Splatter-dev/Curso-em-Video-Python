from datetime import date

ano = int(input('Digite um ano ou digite 0 para analisar o ano atual:  '))

if ano == 0:
    ano = date.today().year
    

def bisex():
    if (ano % 4 == 0) and (ano % 100 > 0) or (ano % 400 == 0):
        print('O ano {} é bixesto!'.format(ano))
    else:
        print('O ano {} não é bisexto!'.format(ano))

bisex()
