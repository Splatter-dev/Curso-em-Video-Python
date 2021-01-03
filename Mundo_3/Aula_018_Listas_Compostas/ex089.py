notas = list()
nomes = list()
aluno = list()
boletim = list()

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    perg = str(input("Deseja continuar [S/N]? ")).strip().upper()
    nomes.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    media = (nota1 + nota2) / 2
    notas.append(media)
    aluno.append(nomes[:])
    aluno.append(notas[:])
    boletim.append(aluno[:])
    if perg == "N":
        break
    else:
        nomes.clear()
        notas.clear()
        aluno.clear()

print("-=" * 15)
print(f"{'No.':^2} {'NOME':^2}     {'MÉDIA':^2}")
print("-" * 30)

for p, l in enumerate(boletim):
    print(f"{p:^2} {l[0][0]:^2}    {l[1][2]:^2}")

print("-=" * 30)

while True:
    codAluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if codAluno == 999:
        break
    for p, l in enumerate(boletim):
        if p == codAluno:
            print(f"As notas de {l[0][0]} são: {l[1][0]} e {l[1][1]}")
print("FIANLIZANDO...")
print(f"{'<<< VOLTE SEMPRE >>>':^15}")


# for c in range(0, len(boletim)):
#     print(f"{(boletim[c][1][0] + boletim[c][1][1]) / 2}")
