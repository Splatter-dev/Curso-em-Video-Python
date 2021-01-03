# for i in range(1,11):
#     print(i)
# print("FIM")

# c = 0

# while c < 10:
#     print(c)
#     c += 1
# print("FIM")

# r = "S"

# while r == "S":
#     n = int(input("Digite um valor:"))
#     r = str(input("Você deseja continuar?[S,N] ")).upper()
# print("FIM")


n = 1
par = impar = 0

while n != 0:
    n = int(input("\nDigite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("{} numeros pares e {} numeros impares.\n".format(par, impar))
