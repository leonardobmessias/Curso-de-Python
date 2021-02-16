valor_casa = float(input('Qual o valor da casa que você quer comprar? '))
valor_salario = float(input('Qual o valor do seu salario ?' ))
qnt_anos = float(input('Quantas anos você pretende pagar? '))
valor_mes = (valor_casa / qnt_anos) / 12
m = valor_salario / 100 * 30
print('Para pagar a casa de R${} em {} anos, a prestação será de R${:.2f}'.format(valor_casa, qnt_anos, valor_mes))
if valor_mes <= m:
    print('Seu emprestimo foi aprovado!')
else:
    print('Seu emprestimo foi negado!')



