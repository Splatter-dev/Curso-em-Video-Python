import datetime as dt

a = dt.datetime.today().year
workList = dict()

workList["nome"] = str(input("Nome: "))
ano = int(input("Ano de nascimento: "))
workList["idade"] = a - ano
ctps = int(input("Carteira de trabalho (0 não tem): "))
if ctps > 0:
    workList["ctps"] = ctps
    anoContrat = int(input("Ano de contratação: "))
    workList["contratacao"] = anoContrat
    idadeAposentadoria = (anoContrat - ano) + 35
    workList["salario"] = float(input("Salário: "))
    workList["aposentadoria"] = idadeAposentadoria
else:
    workList["ctps"] = ctps
print("-=" * 20)

for k, v in workList.items():
    print(f"{k} tem o valor {v}.")
