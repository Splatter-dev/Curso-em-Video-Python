ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    perg = str(input("Deseja continuar [S/N]? ")).strip().upper()
    if perg == "N":
        break
print("-=" * 30)
print(f"{'N.':<4}{'NOME':<10}{'MÉDIA':>8}")
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>6.1f}")

while True:
    codAluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if codAluno == 999:
        break
    for p, l in enumerate(ficha):
        if p == codAluno:
            print(f"As notas de {l[0]} são: {l[1][0]} e {l[1][1]}")
print("FIANLIZANDO...")
print(f"{'<<< VOLTE SEMPRE >>>':^15}")
