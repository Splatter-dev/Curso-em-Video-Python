# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')
nomedivido = nome.split()

print(nome.upper())
print(nome.lower())
print(len(nome))
print(len(nome.replace(' ', ''))) # Tirando espaço entre um nome e outro
print(len(nome) - nome.count(' ')) ## Alternativa para tirar espaços entre um nome e outro
print(len(nomedivido[0])) # Lendo a quantidade de carecteres do primeiro intem da lista(primeiro nome)
print(nome.find(' ')) # Alternativa para ler a quantidade de carecteres do primeiro nome