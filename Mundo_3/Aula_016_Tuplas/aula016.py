lanche = []

lanche = ("Batata Frita", "Hambuguer", "Suco", "Pizza", "Pudim")

print(sorted(lanche))
print(lanche)

print(lanche[-1])
print(len(lanche))
ultimo = len(lanche[-1]) - 1

print(ultimo)

# for c in range(0, ultimo):
#     print(lanche[c])

# for comida in lanche:
#     print(f"Eu vou comer {comida}")

# for pos, comida in enumerate(lanche):
#     print(f"Eu vou comer {comida}, {pos}")

# for c in range(0, len(lanche)):
#     print(f"Eu vou comer {lanche[c]}, {c}")

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)
print(len(c))
print(c.count(5))

print(c.index(2))  # mostrar a posição do numero 2
# print(c.index(5, 1)) # mostrar a posição do numero 5, a partir da posição 1

# pessoa = ("Paulo", 27, "M", 58)
# del(pessoa)
# print(pessoa)