## Relátorio de compras


nameProd = "" 
foward = "S"
totPrice = plus1000 = littlePrice = priceProd = 0
namemPrice = ""


nameProd = input("Nome do Produto: ")
namemPrice = nameProd
priceProd = float(input("Preço: R$ "))
littlePrice = priceProd
totPrice += priceProd
if priceProd >= 1000:
    plus1000 += 1
foward = input("Deseja continuar? [S/N]: ").upper().strip()[0]

while True:
    if foward is "N":
        break

    while foward == "S":
        nameProd = input("Nome do Produto: ")
        priceProd = float(input("Preço: R$ "))

        totPrice += priceProd
        if priceProd >= 1000:
            plus1000 += 1
        if priceProd < littlePrice:
            littlePrice = priceProd
            namemPrice = nameProd

        foward = input("Deseja continuar? [S/N]: ").upper().strip()[0]

    if foward != "S" and foward != "N":
        while foward != "S" and foward != "N":
            foward = input("Deseja continuar? [S/N]: ").upper().strip()[0]

        if foward == "N":
            break
print(
    f"Preço total R${totPrice}. Produtos que custaram mais de R$1000: {plus1000}. Nome do produto mais parato '{namemPrice}' "
)
