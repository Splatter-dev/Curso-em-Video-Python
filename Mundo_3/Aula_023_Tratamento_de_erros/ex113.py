def leiaInt(msgInt):
    print("-" * 30)
    while True:
        try:
            num = int(input(msgInt))
        except (ValueError, TypeError):
            print(f"\033[31m{'ERRO! Digite um número inteiro valido.'}\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\033[31m{'O usuário optou por não digitar o número...'}\033[m")
            return 0
        else:
            return num
            break


def leiaFloat(msgFloat):
    print("-" * 30)
    while True:
        try:
            num = float(input(msgFloat))
        except (ValueError, TypeError):
            print(f"\033[31m{'ERRO! Digite um número real valido.'}\033[m")
        except KeyboardInterrupt:
            print(f"\033[31m{'O usuário optou por não digitar o número...'}\033[m")
            return 0
        else:
            return num
            break


msgInt = leiaInt("Digite um número Inteiro: ")
msgFloat = leiaFloat("Digite um número Real: ")
print(f"O número iteiro é {msgInt} e o real é {msgFloat}.")
