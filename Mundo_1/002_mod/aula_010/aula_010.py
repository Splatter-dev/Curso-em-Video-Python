import emoji

# anos = int(input('Quantos anos o seu carro tem? '))

# def nvvl():
#     if anos <= 3:
#         print('Seu carro é novo!')
#     else:
#         print('Seu carro é velho!')
#     print('________________FIM_________________')            
            

# def nvvl2():
#     print('Seu carro é novo!' if anos <= 3 else 'Seu carro é velho!')


# nome = input('Qual o seu nome?\n').strip().upper()

# def nomecomp():
#     if nome == 'PAULO':
#         print(emoji.emojize('Que nome lindo :grinning:!', use_aliases=True ))
#     else:
#         print(emoji.emojize('Que nome feio  :anguished:!', use_aliases=True))
#     print('Boa noite!!')

# nomecomp()        

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

def mediaf():
    media = (n1 + n2) / 2
    if media >= 5:
        print('Sua nota {:.1f} está acima da média.'.format(media))
    else:
        print('Sua nota {:.1f} está abaixo da média.'.format(media))

mediaf()        