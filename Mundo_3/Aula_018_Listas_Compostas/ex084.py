register = list()
info = list()
greaterW = lowerW = 0
while True:
    info.append(str(input("Nome: ")))
    info.append(float(input("Peso: ")))
    register.append(info[:])
    if len(register) == 1:
        greaterW = lowerW = register[0][1]
    else:
        if info[1] > greaterW:
            greaterW = info[1]
        elif info[1] < lowerW:
            lowerW = info[1]
    info.clear()
    quest = str(input("Deseja continuar [S/N]?")).strip().upper()
    if quest == "N":
        break
print("-=" * 30)
print(f"Ao todo, você cadastrou {len(register)} pessoas.")
print(f"O maior peso foi de {greaterW}kg. Peso de: ", end="")
for weight in register:
    if greaterW == weight[1]:
        print(f"{weight[0]}", end=" ,")
print("")
print(f"O menor peso foi de {lowerW}kg. Peso de: ", end="")
for weight in register:
    if lowerW == weight[1]:
        print(f"{weight[0]}", end=" ,")
