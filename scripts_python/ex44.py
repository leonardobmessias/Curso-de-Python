preco_produto = float(input('Qual o valor do produto?' ))
tipo_pagamento = float(input('Qual o tipo de pagamento? \n1= A VISTA\n2= A VISTA CARTÃO\n3= CARTÃO 2X\n4= CARTÃO 3X OU MAIS!\n'))
if tipo_pagamento == 1:
    print('O valor a ser pago é R${}'.format(preco_produto - (preco_produto/100 * 10)))
elif tipo_pagamento == 2:
    print('O valor a ser pago é R${}'.format(preco_produto - (preco_produto / 100 * 5)))
elif tipo_pagamento == 3:
    print('O valor a ser pago é R${}'.format(preco_produto))
elif tipo_pagamento == 4:
    print('O valor a ser pago é R${}'.format(preco_produto + (preco_produto / 100 * 20)))
else:
    print('Opção invalida de paganeto')