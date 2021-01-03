# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for c, v in enumerate(valores):
#     print(f"Na posição {c} encontrei {v}.")
# print("Cheguei ao final da lista.")


################################################################

# valores = list()
# print(valores)


# for cont in range(0, 5):
#     valores.append(int(input("Digite um numero: ")))
# print(valores)

# for c, v in enumerate(valores):
#     print(f"Na posição {c} encontrei {v}.")
# print("Cheguei ao final da lista.")


####################################################################

a = [2, 3, 4, 7]
# b = a # O Python faz uma ligação de uma lista a outra. B com a A
# b[2] = 8

# print(f"Lista A: {a}")
# print(f"Lista B: {b}")

b = a[:] # Faz uma copia da lista A dentro da lista B
b[2] = 8 
print(f"Lista A: {a}")
print(f"Lista B: {b}")