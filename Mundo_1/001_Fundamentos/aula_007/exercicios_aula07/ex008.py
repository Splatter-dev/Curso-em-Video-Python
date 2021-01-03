# Ler medida dem METROS e converter para CENTIMETROS e MILIMETROS 

mt = float(input('Digite o valor em metros: '))
cm = mt * 100
mm = mt * 1000

print('Conversão em centimetros: {:.0f}cm \n conversão em milimetros: {:.0f}mm'.format(cm, mm))