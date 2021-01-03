matrix = []
listNum = []
totMatrix = matrixP = matrixOdds = matrixThrdColum = matrixScdLine = 0

while totMatrix < 9:
    for p in range(0, 3):
        listNum.append(int(input(f"Digite um valor para: [{len(matrix)}, {p}]: ")))
        totMatrix += 1
        if p == 2:
            matrix.append(listNum[:])
            listNum.clear()
totMatrix = 0

print("-=" * 20)

while totMatrix < 9:
    for p in range(0, 3):
        print(f"[{matrix[matrixP][p]:^5}]", end=" ")
        totMatrix += 1
        if (matrix[matrixP][p]) % 2 == 0:  ## Somar números pares da matriz
            matrixOdds += matrix[matrixP][p]
        if p == 2:  ## Somar valores da terceira coluna da matriz
            matrixThrdColum += matrix[matrixP][p]
        if matrixP == 1:  ## Somar valores da segunda linha
            if matrix[matrixP][p] > matrix[matrixP][0]:
                matrixScdLine = matrix[matrixP][p]
        if p == 2:
            matrixP += 1
            print("")
print("-=" * 20)
print(f"A soma dos valores pares é: {matrixOdds}")
print(f"A soma dos valores da terceira coluna é : {matrixThrdColum}")
print(f"O maior valor da  segunda linha é: {matrixScdLine}")