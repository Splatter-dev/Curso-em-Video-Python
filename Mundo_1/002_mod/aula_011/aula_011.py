    # a = 30
# b = 40

# print('Os números são \033[32m{}\033[m e \033[31m{}\033[m.'.format(a, b))


nome = 'Paulo'

cores = {

    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[m',
    'pretobranco':'\033[7;30m'
}


print('Boa tarde, {}{}{}.'.format(cores['azul'], nome, cores['limpa']))


