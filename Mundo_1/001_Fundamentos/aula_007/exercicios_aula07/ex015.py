## Calcula o valor a pagar pelo aluguel do carro.  60 reais por dia e 0,15 por km.

qtdias = float(input('Digite a quantidade de dias que você ficou com o carro: '))
qtkm = float(input('Digite a quantidade de KM rodados com o carro: '))

vldias = 60 * qtdias
vlkm = 0.15 * qtkm
vltt = vldias + vlkm

print('Valor total dos dias: R${:.2f} \nValor total dos km: R${:.2f} \nValor total a ser pago: R${:.2f}'.format(vldias, vlkm, vltt))