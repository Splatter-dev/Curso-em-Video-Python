estado = dict()
brasil = list()

for c in range(0, 2):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())


# for e in brasil:
#     for uf, sg in e.items():
#         print(f"{uf}: {sg}")

for c in brasil:
    for v in c.values():
        print(v)