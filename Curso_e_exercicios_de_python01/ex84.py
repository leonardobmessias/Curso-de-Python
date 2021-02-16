temp = list()
princ = list()
nomemaiorpeso = list()
nomemenorpeso = list()
maior = menor = 0
cont = 0
cont2 = 0
while True:
    temp.append(str(input('Digite o nome:')))
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])#copia de pessoa
    temp.clear()
    resp = str(input('Quer continuar? ')).lower().strip()[0]
    while resp not in 'sn':
        resp = str(input('Quer continuar? ')).lower().strip()[0]
    if resp == 'n':
        break


print(f'O Total de pessoas cadastradas foi de {len(princ)} pessoas')
print(f'O maior peso foi {maior} Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {menor}  peso de : ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()