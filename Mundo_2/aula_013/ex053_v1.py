## Detector de palíndromo

frase = str(input("\n\nDigite uma frase: ")).strip().upper().replace(" ", "")
inverso = frase[::-1]

print('\nO contrario de "{}" é "{}."\n'.format(frase, inverso))

if inverso == frase:
    print("\nEssa frase é um palindromo!\n")
else:
    print("\nEssa frase não é um palindromo!\n")
