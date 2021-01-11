v = float(input('Qual a velocidade do carro?'))
m = (v - 80) * 7
if v > 80:
    print('Você foi multado em R${}'.format(m))
else:
    print('Tenha um bom dia e dirija com segurança!')
