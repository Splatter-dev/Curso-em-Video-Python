def verVota(anoNasc):
    import datetime as dt
    idade = dt.datetime.today().year - anoNasc
    if idade >= 18 and idade < 65:
        return print(f"VocÊ tem {idade} anos. Seu voto é obrigatorio!")
    elif 15 >= idade  < 18 or idade >= 65:
        return print(f"VocÊ tem {idade} anos. Seu voto é opcional!")
    else:
        return print(f"VocÊ tem {idade} anos. Você ainda não pode votar!")    


print("-" * 30)
anoNasc = int(input("Em que ano você nasceu? "))
vota = verVota(anoNasc)
