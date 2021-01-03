numbers = []
numbersP = []
numbersI = []

while True:
    numbers.append(int(input("Digite um número: ")))
    question = str(input("Deseja continuar [S/N]? ")).strip().upper()
    if question == "N":
        break
for c in numbers:
    if c % 2 == 0:
        numbersP.append(c)
    else:
        numbersI.append(c)

print(f"Lista completa: {numbers}")
print(f"Lista de números par: {numbersP}")
print(f"Lista de números par: {numbersI}")
