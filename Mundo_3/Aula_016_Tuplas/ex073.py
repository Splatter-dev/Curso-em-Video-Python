timesPosi = (
    "Atlético-MG",
    "Internacional",
    "São Paulo",
    "Palmeiras",
    "Vasco",
    "Flamengo",
    "Sport",
    "Santos",
    "Fortaleza",
    "Athletico PR",
    "Fluminense",
    "Ceará",
    "Atlético GO",
    "Grêmio",
    "Corinthians",
    "Curitiba",
    "RB Bragantino",
    "Botafogo",
    "Goiás",
    "Bahia"
)

print(f"Lista de times: {timesPosi} ")
print(f"-*-"*25)
print(timesPosi[0:5])
print(f"-*-"*20)
print(timesPosi[-4:])
print(f"-*-"*40)
print(sorted(timesPosi))
print(f"-*-"*40)
# for pos, nome in enumerate(timesPosi):
#     if nome == "Corinthians":
#          print(f"O  {nome} está em {pos +1}º . ")
print(f"O Corinthians está na  {timesPosi.index('Corinthians') + 1}ª posição.")
