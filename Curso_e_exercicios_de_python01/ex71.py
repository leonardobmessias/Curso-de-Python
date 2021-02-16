valor = 0
valor = int(input('Qual o valor a ser sacado?'))
variavel= variavel2 = variavel3 = 0
retorno = inteiro = 0
while True:
    while True:
        variavel = valor / 50
        inteiro = variavel.__int__()
        valor50 = valor - inteiro * 50
        if inteiro != 0:
            print(f'Total de {inteiro} cédulas de R$50')
        while True:
            variavel2 = valor50 / 20
            variavel2 = variavel2.__int__()
            if variavel2 != 0:
                print(f'Total de {variavel2} cedulas de R$20')
            valor20 = valor50 - variavel2 * 20
            variavel = 0
            if variavel == 0:
                break
        while True:
            variavel3 = (valor20 / 10).__int__()
            if variavel3 != 0:
                print(f'Total de {variavel3} cédulas de R$ 10')
            valor10 = valor20 - variavel3 * 10
            if variavel == 0:
                break
        while True:
            variavel4 = (valor10 / 1).__int__()
            if variavel4  !=0:
                print(f'Total de {variavel4} cédulas de R$1 real')
            if variavel == 0:
                break
        if variavel == 0:
            break
    retorno = variavel * 50
    if variavel == 0:
        break