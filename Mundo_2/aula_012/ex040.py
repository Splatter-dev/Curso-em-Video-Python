# Ler duas notas, calcular média e falar se foi aprovado, reprovado ou ficou de recuperação


print('\nOlá. Seja bem-vindo(a) ao programa de calculo de média.')
nota1 = float(input('\nDigite o valor da primeira nota: '))
ntoa2 = float(input('Digite o valor da segunda nota: '))

media = (nota1 + ntoa2) / 2

if media < 5.0:
    print('\nREPROVADO! Sua media é de {}.\n'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('\nRECUPERAÇÃO! Sua média é de {}.\n'.format(media))
else:
    print('\nAPROVADO! Sua média é de {}.\n'.format(media))        