from time import sleep


def maior(numeros, menorNum, maiorNum):
    print("-=" * 30)
    print("Analisando os valores passados...")
    for c, d in enumerate(numeros):
        print(d, end=" ")
    print(f"Foram informados {len(numeros)} valores ao todo.")
    for c in range(0, len(numeros)):
        if numeros[c] > maiorNum:
            maiorNum = numeros[c]
    print(f"O maior número informado foi {maiorNum}.")



numeros = [2, 9, 4, 5, 7, 1]
menorNum = maiorNum = 0
maior(numeros, menorNum, maiorNum)

numeros = [4, 7, 0]
maior(numeros, menorNum, maiorNum)

numeros = [1, 2]
maior(numeros, menorNum, maiorNum)

numeros = [6]
maior(numeros, menorNum, maiorNum)

numeros = []
maior(numeros, menorNum, maiorNum)