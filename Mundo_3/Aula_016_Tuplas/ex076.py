## IMprimir tupla formatada

shoopList = ("Café", 8.00, "Açucar", 10.0, "Cerveja", 4.0, "Chocolate", 2.50,
            "Leite", 5.50)

print("-" * 40)
print(f"{'LISTA DE COMPRAS':^35}")
print("-" * 40)
ultimo = len(shoopList)
# print(ultimo)

for c in range(0, ultimo, 2):
    print(f"{shoopList[c]:.<30}R${shoopList[c+1]:.2f}")