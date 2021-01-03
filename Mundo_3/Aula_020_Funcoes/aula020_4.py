def dobra(lst):
    pos = 0
    while pos < len(lst):
        # valoresDobrado.append(lst[pos] * 2)
        lst[pos] *= 2
        pos += 1
    # print(lst)


def soma(* numeros):
    s = 0
    for num in numeros:
        s += num
    print(f"Somando os valores {numeros} temos {s}")        


valoresDobrado = []
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
print(valoresDobrado)


soma(5, 2)
soma(2, 9, 4)
