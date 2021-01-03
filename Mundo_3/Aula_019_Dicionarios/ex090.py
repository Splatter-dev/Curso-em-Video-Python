aluno = dict()
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input("Média: "))
if aluno["media"] >= 7:
    aluno["situacao"] = " - Aprovado"
elif 5 < aluno["media"] < 7:
    aluno["situacao"] = " - Recuperação"
else:
    aluno["situacao"] = " - Reprovado"
print(
    f'- O nome é igual: {aluno["nome"]}.\n- A média é: {aluno["media"]}.\n- A situação é:{aluno["situacao"]}'
)
