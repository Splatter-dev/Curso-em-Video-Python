n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
lista = (n1, n2, n3, n4)
print(f"O número 9 apareceu {lista.count(9)} vezes.")
if lista.count(3) > 0:
    print(f"O número 3 apareceu pela primeira vez na {lista.index(3)+1}ª posição.")
else:   
    print("O número 3 não foi digitado.")    
print("Os números pares foram: ",end='')
for numero in lista:
    if numero % 2 == 0:
        print(numero,end=" ")
print("\n")