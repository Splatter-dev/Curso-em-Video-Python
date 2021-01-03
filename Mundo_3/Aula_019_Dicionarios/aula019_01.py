pessoas = {"nome": "Paulo", "sexo": "M", "idade": 27}

print(pessoas["idade"])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


pessoas['nome'] = "Zé"
pessoas['peso'] = 60
del pessoas["sexo"]

for k, v in pessoas.items():
    print(f"{k}: {v}")
