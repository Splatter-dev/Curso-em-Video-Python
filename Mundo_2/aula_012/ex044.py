# Falar o valor do produto, escolher forma de pagamento. De acordo com a forma gerar o valor a ser pago.

print('\nOlá. Seja bem-vindo(a) ao programa de calculo a ser pago pelo produto.')

valorprod = float(input('\nDigite o valor do produto que você está adiquirindo: R$'))

print('\nOpções de pagamento:\n \n1: A vista no dinheiro com desconto de 10%.\n2: À vista no cartão com desconto de 5%.')
print('3: Em até 2x no cartão sem juros.4: \n4: 3x ou mais no cartão com juros de 20%.')

opcsele = str(input('\nDigite o numero da opção de pagamento: '))

tipospag = ['1', '2', '3', '4' ]

if opcsele == tipospag[0]:
    valorfinal = valorprod - (valorprod * 10 / 100)
    print('\nO valor final do produto com desconto de 10% é: R${:.2f}.'.format(valorfinal))
elif opcsele == tipospag[1]:
    valorfinal = valorprod - (valorprod * 5 / 100)
    print('\nO valor final do produto com desconto de 5% é: R${:.2f}.'.format(valorfinal))    
elif opcsele == tipospag[2]:
    valorparcela = valorprod / 2
    print('\nO valor final do produto é: R${:.2f}. Serão duas parcelas de R${:.2f}.'.format(valorprod, valorparcela))
elif opcsele == tipospag[3]:
    valorfinal = valorprod
    qdeparc = int(input('\nQuantas parcelas? '))
    valorfinal = valorprod + (valorprod * 20 / 100)
    valorparcela = valorfinal / qdeparc
    print('\nO valor final do produto ficará em: R${:.2f}. {}x de R${:.2f}.'.format(valorfinal, qdeparc, valorparcela))
else:
    print('Opção de pagamento invalida!')    
