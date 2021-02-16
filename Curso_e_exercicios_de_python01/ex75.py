n = (int(input('Digite um valor:')),
    int(input('Digite mais um valor:')),
    int(input('Digite outro valor:')),
    int(input('Digite o ultimo valor:')))
print(f'Você digitou : {n}')
print(f'O numero 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O numero 3 parece na posição {n.index(3)}')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')
print(f'Os numeros pares são o total:',end='')
for c in n:
    if c % 2 == 0:
        print(c,end=' ')