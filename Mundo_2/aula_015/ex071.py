## Sacar dinheiro e mostras quantas notas sairao. Notas de 50,20,10e 1

print("=" * 30)
print("{:^30}".format("BANCO PV"))
print("=" * 30)

saqueValor = int(input("\nQue valor você quer sacar? R$"))
nota50 = nota20 = nota10 = nota1 = 0

while True:
    if saqueValor == 0:
        break

    else:
        while (
            saqueValor >= 1
        ):  ## Enquanto  houver algum valor que satisfaça os ifs o codigo ira rodar

            if saqueValor >= 50:
                saqueValor -= 50
                nota50 += 1

            else:
                if saqueValor >= 20 < 50:
                    saqueValor -= 20
                    nota20 += 1

                else:
                    if saqueValor >= 10 < 20:
                        saqueValor -= 10
                        nota10 += 1

                    else:
                        if saqueValor >= 1 < 10:
                            saqueValor -= 1
                            nota1 += 1

                        else:
                            break

print("=" * 30)
if nota50 > 0:
    print(f"Total de {nota50} notas de 50.")
if nota20 > 0:
    print(f"Total de {nota20} notas de 20.")
if nota10 > 0:
    print(f"Total de {nota10} notas de 10.")
if nota1 > 0:
    print(f"Total de {nota1} notas de 1.")
print("=" * 30)
