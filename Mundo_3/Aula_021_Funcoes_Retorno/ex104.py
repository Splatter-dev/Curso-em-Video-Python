def leiaInt(msg):
    print("-" * 30)
    while True:
        num = input(f"{msg}").strip()
        if not num.isnumeric():
            print(f"\033[31m{'ERRO! Digite apenas números.'}\033[m")
        else:
            return num
            break


n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}.")

