produto =''
preço = soma = cont = maisbarato = 0
escolha = ''
nomemaisbarato = ''
while True:
    produto = str(input('Qual é o nome do produto? '))
    preço = float(input('Qual o preço deste produto?'))
    if maisbarato == 0:
        maisbarato = preço
    if preço <= maisbarato:
        maisbarato = preço
        nomemaisbarato = produto
    if preço > 1000:
        cont +=1
    soma  = soma + preço
    while True:
        escolha = str(input('Quer continuar? [S/N]')).lower().strip()[0]
        if escolha in 'sn':
            break
    if escolha == 'n':
        break
print(f'O total gasto nos produtos é {soma}')
print(f'{cont} produtos custam mais de R$1000')
print(f'O produto mais caro foi {nomemaisbarato} e custa R${maisbarato}')
print('Fiim')