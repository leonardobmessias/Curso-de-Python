n = float(input('Qual a distancia de sua viagem? '))
if n <= 200:
    print('O Preço da sua pasagem é {}'.format(n * 0.50))
else:
    print('O preço  da sua passaem é {}'.format((n * 0.45)))