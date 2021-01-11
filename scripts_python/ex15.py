km = float(input(' Quantos km rodados?'))
dias = int(input('Qauntos dias usando o carro?'))
calculo = (dias * 60) + (km * 0.15)
print(' o valor de seu aluguel é {:.2f}'.format(calculo))