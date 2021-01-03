numbers = [] 
for c in range(0, 5):
    numbers.append(int(input("Digite um número: ")))
    if c == 0:
        print("Primeiro elemento da lista.")
    else:
        if numbers[c] < numbers[0]:
            numbers.insert(0, numbers[c])
            numbers.pop()
            print(f"Adicionado na posição 0 da lista")
        if numbers[c] < numbers[1]:
            numbers.insert(1, numbers[c])
            numbers.pop()
            print(f"Adicionado na posição 1 da lista")
        if c > 2:
            if numbers[c] < numbers[2]:
                numbers.insert(2, numbers[c])
                numbers.pop()
                print(f"Adicionado na posição 2 da lista")
            if numbers[c] < numbers[3]:
                numbers.insert(3, numbers[c])
                numbers.pop()
                print(f"Adicionado na posição 3 da lista")
print(f"Of números digitados em ordem foram: {numbers}")
