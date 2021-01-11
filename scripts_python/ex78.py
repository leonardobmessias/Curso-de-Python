lista = []
menor = 0
maior = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um numero para posição {c}: ')))
    numero = lista[c]
print(f'A Lista escrita foi: {lista}')
print(f'O número maior é {max(lista)} na posição {lista.index(max(lista))}')
print(f'O numero menor é {min(lista)} nas posiçoes {lista.index(min(lista))}')
