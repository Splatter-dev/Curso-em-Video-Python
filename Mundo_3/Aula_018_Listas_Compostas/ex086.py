matrix = []
listNum = []
totMatrix = lst = 0

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
        print(f"[ {matrix[lst][p]}:^5] ", end=" ")
        totMatrix += 1
        if p == 2:
            lst += 1
            print("")
