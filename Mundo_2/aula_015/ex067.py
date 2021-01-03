# Tabuada

n = 0
result = 0
count = 0
print("\nSeja bem-vindo ao programa de tabuada!")
while True:
    n = int(input("\nDigite um numero: "))
    if n < 0:
        break
    else:
        while count < 10:
            count += 1
            result = n * count
            print(f"{n} x {count} = {result}")
            if count == 10:
                count = 0
                break
print("\nPrograma de tabuada ENCERRADO!Até a próxima!\n")            
        