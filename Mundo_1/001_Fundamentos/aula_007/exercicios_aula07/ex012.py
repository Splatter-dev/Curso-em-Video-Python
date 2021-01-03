# Produto com 5% de desconto

vlpd = float(input('Digite o valor do produto: '))
desc_5 = (vlpd * 5) / 100
vlfn = vlpd - desc_5

print('O valor do desconto é de R${} e o valor final do produto é de R${}'.format(desc_5, vlfn))