## Dector de palíndromo

frase = str(input('\nDigite uma frase: ')).upper()
junto = frase.replace(' ','')
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    # print(junto[letra])
    inverso += junto[letra]

if inverso == junto:
    print('\nA frase "{}" ao contrario é "{}". Essa frase é um palímdromo!\n'.format(junto,inverso))
else:
    print('\nA frase "{}" ao contrario é "{}". Essa frase não é um palindromo!\n'.format(junto,inverso))    




    