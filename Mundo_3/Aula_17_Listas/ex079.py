numbers = []
# print(numbers[0:-1])
while True:
    numbers.append(int(input("Digite um valor: ")))
    if len(numbers) > 1:
        if numbers[-1] in numbers[0:-1]:
            print("Valor duplicado! Não irei adicionar.")
            numbers.pop()
        else:
            print("Valor adicionado com sucesso")
    question = input(("Deseja continuar [S/N]? ")).strip().upper()
    if question == "N":
        break
print(f"Você digitou os valores: {sorted(numbers)}")