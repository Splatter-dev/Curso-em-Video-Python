numbers = list()
smaller = bigger = 0


for c in range(0, 5):
    numbers.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        smaller = bigger = numbers[c]
    else:
        if numbers[c] > bigger:
            bigger = numbers[c]
        if numbers[c] < smaller:
            smaller = numbers[c]

print("-=-" * 13)

print(f"Você digitou: {numbers}")
print("\n")

print(f"O maior número digitado foi {bigger} nas posições: ", end="")
for p, v in enumerate(numbers):  # Posição do maior numero
    if v == bigger:
        print(f"{p}...", end="")

print("\n")

print(f"O menor número foi {smaller} nas pocições: ", end="")
for p, v in enumerate(numbers):
    if v == smaller:
        print(f"{p}...", end="")
print("\n")
