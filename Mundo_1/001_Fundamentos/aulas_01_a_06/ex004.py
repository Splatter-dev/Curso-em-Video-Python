alg = input('Digite algo: ')
print('O valor {} é alfa numerico? '.format(alg), alg.isalnum())
print('O valor {} contem somente letras? '.format(alg), alg.isalpha())
print('O valor {} é decimal? '.format(alg), alg.isdecimal())
print('O valor {} é um digito? '.format(alg), alg.isdigit())
print('O valor {} é um identificador? '.format(alg), alg.isidentifier())
print('O valor {} contem somente letras minusculas? '.format(alg), alg.islower())
print('O valor {} é numerico? '.format(alg), alg.isnumeric())
print('O valor {} é imprimivel? '.format(alg), alg.isprintable())
print('O valor {} tem espaço? '.format(alg), alg.isspace())
print('O valor {} é um titulo? '.format(alg), alg.istitle())
print('O valor {} contem sumento letras maiusculas?'.format(alg), alg.isupper())