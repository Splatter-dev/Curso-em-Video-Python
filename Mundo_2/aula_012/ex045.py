# Jogo Joken Po

from random import choice

print('\nOlá. Vamos jogar Jokênpô? :)')
print('\nAs regras são as seguintes:\n')
print('- Pedra ganha da Tesoura (a amassa e quebra)')
print('- Tesoura ganha do Papel (o corta)')
print('- Papel ganha da Pedra (a embrulha)')
print('- Se os dois jogadores escolherem opções igauis o jogo reinicia! ')


userchoice = str(input('\nAs opções são:\n\nPedra\nPapel\nTesoura\n\nDigite a sua opção: ')).strip().upper()

jokenlist = ['PEDRA','PAPEL','TESOURA']
machinechoice = choice(jokenlist)

print('''\nComputador jogou {}
Jogador jogou {}
'''.format(machinechoice, userchoice))

if userchoice == jokenlist[0] and machinechoice == jokenlist[2]:
    print('Pedra ganha de Tesoura. Você ganhou!\n')
elif userchoice == jokenlist[2] and machinechoice == jokenlist[0]:
    print('Pedra ganha de Tesoura. Você perdeu!\n')
elif userchoice == jokenlist[2] and machinechoice == jokenlist[1]:
    print('Tesoura ganha de Papel. Você Ganhou!\n')
elif userchoice == jokenlist[1] and machinechoice == jokenlist[2]:  
    print('Tesoura ganha de papel. Você perdeu!\n')
elif userchoice == jokenlist[1] and machinechoice == jokenlist[0]:
    print('Papel ganha de Pedra. Você ganhou!\n')
elif userchoice == jokenlist[0] and machinechoice == jokenlist[1]:
    print('Papel ganha de Pedra. Você perdeu!\n')  
elif userchoice != jokenlist[0] and userchoice != jokenlist[1] and userchoice != jokenlist[2] :
    print('Escolha invalida. Escolha novamente!\n')      
else:
    print('Escolhas iguais! Reinicie o jogo!\n')