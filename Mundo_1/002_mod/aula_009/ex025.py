#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite um nome completo: ').strip().title()
print('O nome contem o sobrenome "Silva"? {}'.format('Silva' in nome))