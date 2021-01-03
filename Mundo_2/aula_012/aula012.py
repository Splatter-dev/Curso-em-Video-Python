nome = str(input('Como você se chama?\n').title())

def conversa():
    if nome == 'Paulo':
        print('Que nome lindo, {}.'.format(nome))
    elif nome == 'José' or nome == 'Amanda' or nome == 'Maria':
        print('\nSeu nome é bem popular!')
    elif nome in 'Ana Vanessa Priscila':
        print('Você está ficando com o Paulo, hmm!')        
    else:
        print('\nQue nome comum!')    
    print('Tenha um otimo dia! '.format(nome))    



cores: {
    'limpa ': '\033[m',
    'azul' : '\033[34m',
    'amarelo' : '\033[33m',
    'ptb' : '\033[7;30m'
}

conversa()        
