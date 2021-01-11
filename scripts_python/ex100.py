from random import randint
def sortear(lista):
    print('Sortendo 5 valores da lista: ',end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print('Pronto!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores de {lista}, temos {soma}')
numeros =[]
sortear(numeros)
somapar(numeros)