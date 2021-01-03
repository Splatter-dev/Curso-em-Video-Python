num = [2, 5, 9, 1]
num[2] = 3 # Troca o elemento 9 por 3
num.append(7) # Adiciona o valor 7 no final da lista
# num.insert(2, 0) # Inseri o numero 0 na posição 2
# print(num)
# num.sort()
# print(num)
num.insert(2, 2) # Inseri o numero 2 na posição 2

if 5 in num:
    num.remove(5) # Remove o elemento dentro do (). Varre do inicio ao fim. Remove o primeiro encontrado
    print("Removi o número 5.")
else:
    print("Não achei o número 4.")

# num.sort(reverse=True)
print(num)
print(f"Essa lista tem {len(num)} elementos.")

#############

# num.pop(2)
# print(num)
# print(f"Essa lista tem {len(num)} elementos.")