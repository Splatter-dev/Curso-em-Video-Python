def calculo(lg, cp):
    area = lg * cp
    print(f"A área de um terreno {lg}x{cp} é de {area}m². ")


print("Controle de Terrenos")
print("-" * 20)
largura = float(input("Largura (m): "))
comprimmento = float(input("Comprimento (m): "))
calculo(largura, comprimmento)
