# Natação: Até 9 anos Mirim, Até 14 Infantil, Até 19 Jnior, Até 20 Senior, Acima de 20 Master

from datetime import date

print('\nOlá. Seja bem-vindo(a) ao programa de natação.')
anonasc = int(input('\nQual o ano do seu nascimento? '))

anoatual = date.today().year
idade = anoatual - anonasc

print('\nO atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('\nVocê se encaixa na categoria Mirim.\n')
elif idade > 9 and idade <= 14:
    print('\nVocê se encaixa na categoria Infaltil.\n') 
elif idade > 14 and idade <= 19:
    print('\nVocê se encaixa na categoria Junior.\n')
elif idade > 19 and idade <= 25:
    print('\nVocê se encaixa na categoria Senior.\n')   
else:
    print('\nVocê se encaixa na categoria Master.\n')