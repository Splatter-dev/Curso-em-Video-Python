# Calcular area em m² e quantidade de tinta para pintar a area sabendo que cada litro pinta 2m²

alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))

m2 = alt * larg
tin1 = 2 
tinnc = (m2 * 1) / tin1

print('A medida de parede é {}m² e a quantidade de tinta necessaria é {:.3f} litros'.format(m2, tinnc))
