from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)
num3 = randint(1, 10)
num4 = randint(1, 10)
num5 = randint(1, 10)
lista = (num1, num2, num3, num4, num5)

c = 1
maior = lista[0]
menor = lista[0]

while c < 5:
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]
    c += 1
print(f"Numeros: {num1} {num2} {num3} {num4} {num5}")
print(f"O maior número foi: {maior}")
print(f"O menor número foi: {menor}")

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print("Os numeros sorteados foram: ",end='')
for numeros in n:
    print(f"{numeros}", end=' ')
print("\n")      
print(f"O maior valor sorteado foi: {max(n)}")
print(f"O menor valor sorteado foi: {min(n)}")


# for c in range(0,5):
#     print(f"{n[c]}",end=' ')
# print("")    
