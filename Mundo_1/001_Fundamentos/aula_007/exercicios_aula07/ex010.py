# Transformar real em dolar

cart = float(input('Digite o valor que você tem na carteira: R$'))
pcdoll = 3.27
doll = (cart * 1) / pcdoll
print('Dolars que você pode comprar US${:.2f}'.format(doll))
