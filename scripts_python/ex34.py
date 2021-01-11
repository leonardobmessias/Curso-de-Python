sal = float(input('Qual o valor do seu salario?'))
if sal > 1250:
    print('Seu almento é de {}'. format(sal/100*10+sal))
else:
    print('Seu salario é de {}'.format(sal / 100 * 15 + sal))
