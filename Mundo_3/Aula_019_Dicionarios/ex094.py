infoPessoas = list()
infos = dict()
totIdade = 0
mediaIdade = 0

while True:
    nome = str(input("Nome: "))
    sexo = str(input("Sexo [F/M]: ")).upper().strip()
    idade = int(input("Idade: "))
    continuar = str(input("Deseja continuar [S/N]? ")).upper().strip()
    for c in range(0, 3):
        infos = {"nome": nome, "sexo": sexo, "idade": idade}
    infoPessoas.append(infos)
    if continuar == "N":
        break
for v in infoPessoas:
    totIdade = totIdade + v["idade"]

mediaIdade = totIdade / len(infoPessoas)
print("-=" * 30)
print(f"- O grupo tem {len(infoPessoas)} pessoas.")
print(f"- A média de idade do grupo é de {mediaIdade:.2f} anos.")
print(f"- As mulheres cadastradas foram: ", end="")
for v in infoPessoas:
    if v["sexo"] == "F":    
        print(f'{v["nome"]}', end=" ")
print("")        
print("- Lista das pessoas que estão acima da média: ")
print("")
for v in infoPessoas:
    if v["idade"] > mediaIdade:
        print(f'nome = {v["nome"]}, sexo = {v["sexo"]}, idade = {v["idade"]}')
print("<<< ENCERRADO >>>")        
