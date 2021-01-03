# Calcular valor de prestação e comparar se o valor não excede 30% do salário da cliente.

def mensagemrepro():
    print('Seu emprestimo foi negado!')
    print('Salário: R${:.2f}\nTrinta por cento do salario: R${:.2f}\nQuantidade de parcelas: {}\nValor da prestação: R${:.2f}'.format(salario,salario30, meses,valorpresta))


def mensagemapro():
    print('Seu emprestimo foi aceito, parabéns!')
    print('Salário: R${:.2f}\nTrinta por cento do salario: R${:.2f}\nQuantidade de parcelas: {}\nValor da prestação: R${:.2f}'.format(salario,salario30, meses,valorpresta))


precocasa = float(input('Seja bem-vindo ao programa de Emprestimo. Qual o valor da casa que você deseja comprar?\nR$'))
salario = float(input('Qual o valor do seu salario?\nR$'))
anosparc = int(input('Em quantos anos você deseja pagar?\n'))

meses = 12 * anosparc
valorpresta = precocasa / (12 * anosparc)
salario30 = salario * 30 / 100  

if valorpresta <= salario30:
    mensagemapro()
else:
    mensagemrepro()   