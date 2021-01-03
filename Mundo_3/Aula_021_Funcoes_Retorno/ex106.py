





        
        


print("~"*30)
print("   SISTEMA DE AJUDA PyHELP")
print("~"*30)
cmd = ""
while cmd != "fim":
    cmd = str(input("Função ou biblioteca > ")).lower().strip()
    while cmd != "fim":
        teste = (help(cmd))
        print("oi", exit)
    else:
        break