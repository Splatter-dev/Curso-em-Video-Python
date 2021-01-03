express = []
contAbre = 0
contFecha = 0
express.append(input("Digite a expressão: "))

for elemento in express:
    for c in elemento:
        if c == "(":
            contAbre += 1
for elemento in express:
    for c in elemento:
        if c == ")":
            contFecha += 1       

if contAbre == contFecha:
    print("Expressão válida!")
else:
    print("Expressão inválida!")

# test = express[0]
# print(test.split())
# print(test.count("("))