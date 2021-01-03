# Calcular acrescimo de 15% de salario

sl = float(input('Valor do salário a ser aumentado:R$ '))
vlrac = (sl * 15) / 100
slf = sl + vlrac
print('O valor do aumento será de R${:.2f} e o valor final do salario será de R${:.2f}'.format(vlrac, slf))
