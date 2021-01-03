#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ')

def prinome():
    firstname = nome.split()
    return print('O primeiro nome é: {}'.format(firstname[0]))

def segunome(): # itens de uma lista são contados do 0 em diante, ex: 0,1,2,3 = 4 numeros
    lastname = nome.split() # Divide a string em lista
    # print(lastname) # Imprime os elementos da lista
    # print(len(lastname)) # Imprime o numero da quantidade de itens da lista
    indice = len(lastname) -1 # função len transforma para numero para poder conta , o -1 subtrai 1 numero(não subtra item da lista) o valor é atribuido a variavel indice
    # print(indice) # Imprime o numero da quantidade de itens atulizado com - 1
    ultindice = lastname[indice] # Aqui a variavel ultindice recebe o valor do ultimo item da lista, que é passado atraves da variavel indice que representa em numero aultima posição da lista 
    return print('O ultimo nome é: {}'.format(ultindice))    # Imprime o ultimo idice da lista 

def segunomeatu(): # Método simplificado para conseguir o ultimo item da lista
    lastname = nome.split()
    return print('O ultimo nome é: {}'.format(lastname[-1]))

prinome()    
segunome()
segunomeatu()