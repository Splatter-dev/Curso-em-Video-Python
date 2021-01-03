from time import sleep

def contador(inicio, fim, param):
    if param == 0:
        param += 1
    print("-=" * 30)
    print(f"Contagem de {inicio} até {fim} de {param} em {param}: ")
    if fim > inicio:
        tot = inicio
        while tot <= fim:
            print(tot, end=" ", flush=True)
            sleep(0.1)
            tot += abs(param)
    if fim < inicio or param < 0:
        tot = inicio
        while tot >= fim:
            print(tot, end=" ", flush=True)
            sleep(0.1)
            tot -= abs(param)
    print("FIM!")


inicio = 1
fim = 10
param = 1
contador(inicio, fim, param)

inicio = 10
fim = 0
param = 2
contador(inicio, fim, param)

print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
param = int(input("Passo: "))
contador(inicio, fim, param)