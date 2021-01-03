numbers = []
while True:
    numbers.append(int(input("Digite um número: ")))
    question = input("Deseja continuar [S/N]? ").strip().upper()
    if question == "N":
        break
print(f"\nForam digitados {len(numbers)} números.")
print(f"Ordem decrescente da lista: {sorted(numbers, reverse=True)}")

if 5 in numbers:
    print(f"Tem número 5 na lista. Ele está na posição: ",end="")
    for p, c in enumerate(numbers):
        if c == 5:
            print(f"{p}...",end="")
    print("")    
else:
    print("O número 5 não está na lista!")
