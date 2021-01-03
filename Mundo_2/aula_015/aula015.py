n = s = 0
count = 0
while True:
    n = int(input("\nDigite um número:"))
    if n == 999:
        break
    s += n 
    count += 1
print(f"A soma vale {s} e foram digitados {count} números.")    