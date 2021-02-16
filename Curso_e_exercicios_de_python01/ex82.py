lista = []
listapar = []
listaimpar= []
while True:
    lista.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar? ')).lower().strip()[0]
    if resp in 'n':
        break
for c in lista:
    if c %2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print(f'Lista total: {lista}')
print(f'Lista de numeros pares: {listapar}')
print(f'Lista com numeros impares: {listaimpar}')