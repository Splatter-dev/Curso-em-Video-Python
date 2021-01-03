#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome de uma cidade: ').title().split()
# cidadediv = cidade.title().split()
print('A cidade contem a palavra "Santo": {} '.format('Santo' in cidade[0]))