matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para a [{l}, {c}]: "))
print("-=" * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[ {matriz[l][c]:^5}] ", end="")
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if c == 2:
            scol += matriz[l][c]
        if l == 1:  
            if matriz[l][c] > mai:
                mai = matriz[l][c]

    print("")
print("-=" * 20)
print(f"A soma dos valores pares é: {spar}")
print(f"A soma dos valores da terceira coluna é: {scol}")
print(f"O maior valor da segunda linha é: {mai}")


## :^5 são 5 espaços centralizados