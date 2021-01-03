numbersList = [[], []]
for c in range(0, 7):
    n = int(input(f"Digite o {c+1}° valor: "))
    if n % 2 == 0:
        numbersList[0].append(n)
    else:
        numbersList[1].append(n)
print(f"Os valores pares digitados foram: {sorted(numbersList[0])}")
print(f"Os valores ímpares digitados foram: {sorted(numbersList[1])}")